import streamlit as st
import folium
from streamlit_folium import st_folium
from utils.jeju_olle import JEJU_OLLE_COURSES, JEJU_THEMES, HIGHLIGHT_COORDS
from utils.seoul_courses import SEOUL_COURSES, SEOUL_HIGHLIGHT_COORDS, SEOUL_THEMES
from utils.busan_courses import BUSAN_COURSES, BUSAN_HIGHLIGHT_COORDS, BUSAN_THEMES
from api.claude_api import curate_in_english, generate_plogging_route
from api.tour_api import get_nearby_restaurants, get_nearby_accommodations, format_place

st.set_page_config(page_title="Course Finder", page_icon="🗺️", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #F7F3EE; }
[data-testid="stSidebar"] { background-color: #EDE8E0; }
.course-header {
    background: linear-gradient(135deg, #2D6A4F, #40916C);
    color: white;
    padding: 24px 28px;
    border-radius: 16px;
    margin-bottom: 20px;
}
.course-header h2 { color: white; margin: 0 0 8px 0; font-size: 1.6rem; }
.course-header p { color: #B7E4C7; margin: 0; font-size: 0.95rem; }
.info-banner {
    background: #D8F3DC;
    border-left: 4px solid #2D6A4F;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 16px;
    color: #1B4332;
    font-size: 0.95rem;
}
.metric-card {
    background: white;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    border: 1px solid #D4C9B8;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.metric-card .value { font-size: 1.8rem; font-weight: 700; color: #2D6A4F; }
.metric-card .label { font-size: 0.8rem; color: #888; margin-top: 4px; }
.route-box {
    background: white;
    border-left: 4px solid #40916C;
    border-radius: 10px;
    padding: 20px;
    font-size: 0.92rem;
    line-height: 1.9;
    color: #2d2d2d;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.tip-box {
    background: #F0FFF4;
    border: 1px dashed #40916C;
    border-radius: 10px;
    padding: 14px 16px;
    color: #1B4332;
    font-size: 0.9rem;
    margin-top: 12px;
}
.place-card {
    background: white;
    border-radius: 10px;
    padding: 12px;
    margin-bottom: 8px;
    border: 1px solid #E0D9CE;
}
h3 { color: #2D6A4F; }
</style>
""", unsafe_allow_html=True)

REGION_DATA = {
    "🌿 Jeju": {
        "courses": JEJU_OLLE_COURSES,
        "themes": JEJU_THEMES,
        "coords": HIGHLIGHT_COORDS,
    },
    "🏙️ Seoul": {
        "courses": SEOUL_COURSES,
        "themes": SEOUL_THEMES,
        "coords": SEOUL_HIGHLIGHT_COORDS,
    },
    "🌊 Busan": {
        "courses": BUSAN_COURSES,
        "themes": BUSAN_THEMES,
        "coords": BUSAN_HIGHLIGHT_COORDS,
    },
}

for key in ["selected_course", "route", "descriptions", "restaurants", "accommodations", "highlight_coords"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "descriptions" else {}

# ── 사이드바 ──
with st.sidebar:
    st.markdown("## 🌿 Find Your Route")
    st.markdown("---")

    region = st.selectbox("🗺️ Region", list(REGION_DATA.keys()))
    region_info = REGION_DATA[region]
    all_themes = region_info["themes"]
    highlight_coords = region_info["coords"]

    difficulty_filter = st.selectbox("💪 Difficulty", ["All", "Easy", "Moderate", "Challenge"])
    theme_filter = st.selectbox(
        "🎨 Theme", ["All"] + list(all_themes.keys()),
        format_func=lambda x: "All Themes" if x == "All" else all_themes[x]
    )
    pet_filter = st.checkbox("🐾 Pet-friendly only")
    st.markdown("---")

    courses = region_info["courses"]
    if difficulty_filter != "All":
        courses = [c for c in courses if c["difficulty"] == difficulty_filter]
    if theme_filter != "All":
        courses = [c for c in courses if c["theme"] == theme_filter]
    if pet_filter:
        courses = [c for c in courses if c["pet_friendly"]]

    st.caption(f"🗺️ {len(courses)} courses found")

    if courses:
        course_names = [f"{c['name']} ({c['distance_km']}km)" for c in courses]
        selected_idx = st.selectbox("📍 Select Course", range(len(courses)),
                                    format_func=lambda i: course_names[i])
        selected_course = courses[selected_idx]

        st.markdown("---")
        st.markdown(f"""
        <div style='background:white;border-radius:12px;padding:14px;border:1px solid #D4C9B8;'>
            <div style='font-size:0.85rem;color:#888;margin-bottom:8px'>Selected Course</div>
            <div style='font-weight:700;color:#2D6A4F;font-size:1rem;margin-bottom:10px'>{selected_course['name_en']}</div>
            <div style='font-size:0.85rem;'>
                ⏱️ {selected_course['duration_hours']}h &nbsp;
                📏 {selected_course['distance_km']}km &nbsp;
                🐾 {'✅' if selected_course['pet_friendly'] else '❌'}
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("")

        if st.button("🏃 Start This Route", type="primary", use_container_width=True):
            st.session_state.selected_course = selected_course
            st.session_state.highlight_coords = highlight_coords
            st.session_state.route = None
            st.session_state.descriptions = {}
            st.session_state.restaurants = None
            st.session_state.accommodations = None
    else:
        st.warning("No courses match. Try adjusting filters.")
        st.session_state.selected_course = None

# ── 메인 화면 ──
if st.session_state.selected_course:
    course = st.session_state.selected_course
    highlight_coords = st.session_state.highlight_coords or HIGHLIGHT_COORDS

    if st.button("← Back to All Courses"):
        st.session_state.selected_course = None
        st.session_state.route = None
        st.session_state.descriptions = {}
        st.session_state.restaurants = None
        st.session_state.accommodations = None
        st.rerun()

    theme_emoji = {"coastal": "🌊", "island": "🏝️", "forest": "🌲", "rural": "🌾",
                   "urban": "🏙️", "mountain": "⛰️", "nature": "🌿", "park": "🌳",
                   "beach": "🏖️", "heritage": "🏛️"}

    st.markdown(f"""
    <div class='course-header'>
        <h2>{theme_emoji.get(course['theme'], '🌿')} {course['name_en']}</h2>
        <p>{course['description_en']}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='metric-card'><div class='value'>{course['distance_km']}km</div><div class='label'>Distance</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><div class='value'>{course['duration_hours']}h</div><div class='label'>Duration</div></div>", unsafe_allow_html=True)
    with col3:
        diff_color = {"Easy": "#2D6A4F", "Moderate": "#856404", "Challenge": "#842029"}[course['difficulty']]
        st.markdown(f"<div class='metric-card'><div class='value' style='color:{diff_color};font-size:1.4rem'>{course['difficulty']}</div><div class='label'>Difficulty</div></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='metric-card'><div class='value' style='font-size:1.1rem'>{'🐾 Yes' if course['pet_friendly'] else '❌ No'}</div><div class='label'>Pet-friendly</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='info-banner'>
        🚩 <b>Start:</b> {course['start_en']} &nbsp;→&nbsp; 🏁 <b>End:</b> {course['end_en']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # TourAPI 먼저 로드
        # TourAPI 먼저 로드
    if st.session_state.restaurants is None:
        try:
            st.session_state.restaurants = get_nearby_restaurants(course["lat"], course["lon"])
        except:
            st.session_state.restaurants = []
    if st.session_state.accommodations is None:
        try:
            st.session_state.accommodations = get_nearby_accommodations(course["lat"], course["lon"])
        except:
            st.session_state.accommodations = []

    # 지도
    st.markdown("### 🗺️ Route Map")
    all_lats = [course['lat']]
    all_lons = [course['lon']]
    for h in course['highlights_en']:
        if h in highlight_coords:
            all_lats.append(highlight_coords[h][0])
            all_lons.append(highlight_coords[h][1])
    center_lat = sum(all_lats) / len(all_lats)
    center_lon = sum(all_lons) / len(all_lons)

    m = folium.Map(location=[center_lat, center_lon], zoom_start=13, tiles="OpenStreetMap")

    # 시작점
    folium.CircleMarker(
        location=[course['lat'], course['lon']],
        radius=14, color="white", fill=True,
        fill_color="#2D6A4F", fill_opacity=1.0,
        popup=folium.Popup(f"<b>🚩 Start: {course['start_en']}</b>", max_width=200),
        tooltip=f"🚩 Start: {course['start_en']}"
    ).add_to(m)

    # 하이라이트 핀
    colors = ["blue", "purple", "orange", "red", "darkblue"]
    highlight_coords_list = []
    for i, highlight in enumerate(course['highlights_en']):
        if highlight in highlight_coords:
            coords = highlight_coords[highlight]
            highlight_coords_list.append(coords)
            folium.Marker(
                location=coords,
                popup=folium.Popup(f"⭐ {highlight}", max_width=200),
                tooltip=f"{i+1}. {highlight}",
                icon=folium.Icon(color=colors[i % len(colors)], icon="star", prefix="fa")
            ).add_to(m)


    # 음식점 핀
    if st.session_state.restaurants:
        for r in st.session_state.restaurants[:4]:
            p = format_place(r)
            if p['lat'] and p['lon']:
                try:
                    folium.Marker(
                        location=[float(p['lat']), float(p['lon'])],
                        popup=folium.Popup(f"🍜 {p['title']}<br>{p['addr']}", max_width=200),
                        tooltip=f"🍜 {p['title']}",
                        icon=folium.Icon(color="red", icon="cutlery", prefix="fa")
                    ).add_to(m)
                except:
                    pass

    # 숙박 핀
    if st.session_state.accommodations:
        for a in st.session_state.accommodations[:4]:
            p = format_place(a)
            if p['lat'] and p['lon']:
                try:
                    folium.Marker(
                        location=[float(p['lat']), float(p['lon'])],
                        popup=folium.Popup(f"🏨 {p['title']}<br>{p['addr']}", max_width=200),
                        tooltip=f"🏨 {p['title']}",
                        icon=folium.Icon(color="cadetblue", icon="bed", prefix="fa")
                    ).add_to(m)
                except:
                    pass

    # 범례
    legend_html = """
    <div style='position:fixed;bottom:30px;left:50px;z-index:1000;
                background:white;padding:10px 14px;border-radius:8px;
                border:1px solid #ccc;font-size:12px;line-height:2;
                box-shadow:2px 2px 6px rgba(0,0,0,0.15)'>
        🟢 Start Point<br>⭐ Highlights<br>→ Route Direction<br>🔴 Restaurants<br>🔵 Accommodations
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    st_folium(m, width=None, height=450, returned_objects=[])


       # 공식 지도 버튼
    st.markdown("#### 🗺️ View Official Route Map")
    st.caption("Our map shows key highlights. For the exact trail route, use the official maps below.")
    map_col1, map_col2 = st.columns(2)
    with map_col1:
        if course.get("official_map_url"):
            # 지역별 버튼 텍스트/색상 구분
            if "seoul.go.kr" in course["official_map_url"]:
                btn_label = "🗺️ Smart Seoul Map (Official)"
                btn_color = "#2D6A4F"
                btn_text_color = "white"
            elif "busan.go.kr" in course["official_map_url"]:
                btn_label = "🗺️ Galmaetgil Official Site"
                btn_color = "#0066CC"
                btn_text_color = "white"
            else:
                btn_label = "🗺️ Official Map"
                btn_color = "#2D6A4F"
                btn_text_color = "white"
            st.markdown(f"""
            <a href='{course["official_map_url"]}' target='_blank'>
                <button style='width:100%;background:{btn_color};color:{btn_text_color};border:none;
                              padding:12px;border-radius:8px;cursor:pointer;font-size:1rem;
                              font-weight:600;margin-top:4px'>
                    {btn_label}
                </button>
            </a>
            """, unsafe_allow_html=True)
    with map_col2:
        if course.get("kakao_map_url"):
            st.markdown(f"""
            <a href='{course["kakao_map_url"]}' target='_blank'>
                <button style='width:100%;background:#FEE500;color:#3C1E1E;border:none;
                              padding:12px;border-radius:8px;cursor:pointer;font-size:1rem;
                              font-weight:600;margin-top:4px'>
                    🗺️ KakaoMap
                </button>
            </a>
            """, unsafe_allow_html=True)


    st.markdown("---")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### ⭐ Highlights")
        for i, h in enumerate(course['highlights_en']):
            key = f"{course['id']}_{i}"
            with st.expander(f"{i+1}. {h}"):
                if key not in st.session_state.descriptions:
                    with st.spinner("Generating description..."):
                        try:
                            desc = curate_in_english({"title": h, "addr1": course['start_en']})
                            st.session_state.descriptions[key] = desc
                        except Exception:
                            st.session_state.descriptions[key] = "⏳ Description unavailable. Please try again later."
                st.write(st.session_state.descriptions[key])

        st.markdown(f"""
        <div class='tip-box'>♻️ <b>Plogging Tip:</b> {course['plogging_tip']}</div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🏃 Suggested Plogging Route")
        if not st.session_state.route:
            with st.spinner("Creating your plogging route..."):
                try:
                    places = [{"title": h, "addr1": course["start_en"]} for h in course["highlights_en"]]
                    st.session_state.route = generate_plogging_route(places, course["difficulty"])
                except Exception:
                    st.session_state.route = "⏳ Route generation unavailable. Please try again later."

        st.markdown(
            f'<div class="route-box">{st.session_state.route.replace(chr(10), "<br>")}</div>',
            unsafe_allow_html=True
        )

    # After Your Plogging
    st.markdown("---")
    st.markdown("### 🍽️ After Your Plogging")
    st.caption("Nearby spots powered by 한국관광공사 OpenAPI")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🍜 Nearby Restaurants")
        if st.session_state.restaurants:
            for r in st.session_state.restaurants[:4]:
                p = format_place(r)
                kakao_url = f"https://map.kakao.com/link/search/{p['title']}"
                st.markdown(f"""
                <div class='place-card'>
                    <div style='font-weight:600;color:#2D6A4F;'>
                        <a href='{kakao_url}' target='_blank' style='color:#2D6A4F;text-decoration:none;'>{p['title']} 🔗</a>
                    </div>
                    <div style='font-size:0.82rem;color:#888;'>📍 {p['addr']}</div>
                    <div style='font-size:0.82rem;color:#888;'>📏 {p['dist']}km away</div>
                    {f"<div style='font-size:0.82rem;color:#888;'>📞 {p['tel']}</div>" if p['tel'] else ""}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No restaurants found nearby.")

    with col2:
        st.markdown("#### 🏨 Nearby Accommodations")
        if st.session_state.accommodations:
            for a in st.session_state.accommodations[:4]:
                p = format_place(a)
                kakao_url = f"https://map.kakao.com/link/search/{p['title']}"
                st.markdown(f"""
                <div class='place-card'>
                    <div style='font-weight:600;color:#2D6A4F;'>
                        <a href='{kakao_url}' target='_blank' style='color:#2D6A4F;text-decoration:none;'>{p['title']} 🔗</a>
                    </div>
                    <div style='font-size:0.82rem;color:#888;'>📍 {p['addr']}</div>
                    <div style='font-size:0.82rem;color:#888;'>📏 {p['dist']}km away</div>
                    {f"<div style='font-size:0.82rem;color:#888;'>📞 {p['tel']}</div>" if p['tel'] else ""}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No accommodations found nearby.")

else:
    # 초기 화면
    st.markdown("# 🌿 K-Plogging Trail Courses")
    st.markdown("Select a region and course to get started!")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["🌿 Jeju", "🏙️ Seoul", "🌊 Busan"])

    for tab, (region_name, region_info) in zip([tab1, tab2, tab3], REGION_DATA.items()):
        with tab:
            for theme, theme_label in region_info["themes"].items():
                theme_courses = [c for c in region_info["courses"] if c["theme"] == theme]
                if not theme_courses:
                    continue
                st.markdown(f"### {theme_label}")
                cols = st.columns(min(len(theme_courses), 3))
                for i, course in enumerate(theme_courses):
                    with cols[i % 3]:
                        diff_color = {"Easy": "#2D6A4F", "Moderate": "#856404", "Challenge": "#842029"}[course['difficulty']]
                        pet_icon = "🐾" if course['pet_friendly'] else ""
                        st.markdown(
                            f"<div style='background:white;border-radius:12px;padding:16px;"
                            f"border:1px solid #D4C9B8;margin-bottom:8px;"
                            f"box-shadow:0 2px 8px rgba(0,0,0,0.06);min-height:140px'>"
                            f"<div style='font-weight:700;color:#2D6A4F;margin-bottom:6px'>{course['name_en']}</div>"
                            f"<div style='font-size:0.82rem;color:#666;margin-bottom:10px'>{course['description_en'][:80]}...</div>"
                            f"<div style='font-size:0.8rem;'>📏 {course['distance_km']}km &nbsp;"
                            f"⏱️ {course['duration_hours']}h &nbsp;"
                            f"<span style='color:{diff_color};font-weight:600'>{course['difficulty']}</span>"
                            f"&nbsp;{pet_icon}</div>"
                            f"</div>",
                            unsafe_allow_html=True
                        )
                        if st.button("View Route →", key=f"btn_{course['id']}"):
                            st.session_state.selected_course = course
                            st.session_state.highlight_coords = region_info["coords"]
                            st.session_state.route = None
                            st.session_state.descriptions = {}
                            st.session_state.restaurants = None
                            st.session_state.accommodations = None
                            st.rerun()
                st.markdown("")