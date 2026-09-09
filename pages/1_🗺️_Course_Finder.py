import streamlit as st
import folium
import logging

logger = logging.getLogger(__name__)
from streamlit_folium import st_folium
from utils.jeju_olle import JEJU_OLLE_COURSES, JEJU_THEMES, HIGHLIGHT_COORDS
from utils.seoul_courses import SEOUL_COURSES, SEOUL_HIGHLIGHT_COORDS, SEOUL_THEMES
from utils.busan_courses import BUSAN_COURSES, BUSAN_HIGHLIGHT_COORDS, BUSAN_THEMES
from api.gemini_api import curate_in_english, generate_plogging_route
from api.tour_api import get_nearby_restaurants, get_nearby_accommodations
from utils.ui_components import inject_course_finder_css, render_course_detail, render_nearby_spots
from utils.map_builder import build_course_map, add_poi_markers

st.set_page_config(page_title="Course Finder", page_icon="🗺️", layout="wide")

inject_course_finder_css()

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

# session_state 초기화
for key in ["selected_course", "route", "descriptions", "restaurants", "accommodations", "highlight_coords"]:
    if key not in st.session_state:
        st.session_state[key] = None if key != "descriptions" else {}
if "current_region" not in st.session_state:
    st.session_state.current_region = "🌿 Jeju"

# ── 사이드바 ──
with st.sidebar:
    st.markdown("## 🌿 Find Your Route")
    st.markdown("---")

    region_keys = list(REGION_DATA.keys())
    region = st.selectbox(
        "🗺️ Region", region_keys,
        index=region_keys.index(st.session_state.current_region)
    )
    st.session_state.current_region = region
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
        <div style='background:white;border-radius:12px;padding:14px;border:1px solid {CARD_BORDER};'>
            <div style='font-size:0.85rem;color:{TEXT_MUTED};margin-bottom:8px'>Selected Course</div>
            <div style='font-weight:700;color:{CARD_VALUE};font-size:1rem;margin-bottom:10px'>{selected_course['name_en']}</div>
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
            st.session_state.current_region = region
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

    render_course_detail(course)

    st.markdown("---")

    # TourAPI 로드
    if st.session_state.restaurants is None:
        try:
            st.session_state.restaurants = get_nearby_restaurants(course["lat"], course["lon"])
        except Exception as e:
            logger.warning(f"Failed to fetch restaurants for course {course['id']}: {e}")
            st.session_state.restaurants = []
    if st.session_state.accommodations is None:
        try:
            st.session_state.accommodations = get_nearby_accommodations(course["lat"], course["lon"])
        except Exception as e:
            logger.warning(f"Failed to fetch accommodations for course {course['id']}: {e}")
            st.session_state.accommodations = []

    # 지도
    st.markdown("### 🗺️ Route Map")
    m = build_course_map(course, highlight_coords)
    m = add_poi_markers(m, st.session_state.restaurants, st.session_state.accommodations)
    st_folium(m, width=None, height=450, returned_objects=[])

    # 공식 지도 버튼
    st.markdown("#### 🗺️ View Official Route Map")
    st.caption("Our map shows key highlights. For the exact trail route, use the official maps below.")
    map_col1, map_col2 = st.columns(2)
    with map_col1:
        if course.get("official_map_url"):
            if "seoul.go.kr" in course["official_map_url"]:
                btn_label = "🗺️ Smart Seoul Map (Official)"
                btn_color = BTN_PRIMARY
            elif "busan.go.kr" in course["official_map_url"]:
                btn_label = "🗺️ Galmaetgil Official Site"
                btn_color = BTN_SECONDARY
            elif "jejuolle.org" in course["official_map_url"]:
                btn_label = "🌿 Jeju Olle Official Map"
                btn_color = BTN_TERTIARY
            else:
                btn_label = "🗺️ Official Map"
                btn_color = BTN_PRIMARY
            st.markdown(f"""
            <a href='{course["official_map_url"]}' target='_blank'>
                <button style='width:100%;background:{btn_color};color:white;border:none;
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
                <button style='width:100%;background:{KAKAO_BG};color:{KAKAO_TEXT};border:none;
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
                        except Exception as e:
                            logger.error(f"Failed to generate description for highlight {h} in course {course['id']}: {e}")
                st.write(st.session_state.descriptions.get(key, "⏳ Description unavailable. Please try again later."))

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
                except Exception as e:
                    logger.error(f"Failed to generate plogging route for course {course['id']}: {e}")

        route_text = st.session_state.route or "⏳ Route generation unavailable. Please try again later."
        st.markdown(
            f'<div class="route-box">{route_text.replace(chr(10), "<br>")}</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    render_nearby_spots(course, st.session_state.restaurants, st.session_state.accommodations)

else:
    # 초기 화면
    st.markdown("# 🌿 K-Plogging Trail Courses")
    st.markdown("Select a region and course to get started!")
    st.markdown("---")

    region_choice = st.radio(
        "Select Region",
        list(REGION_DATA.keys()),
        index=list(REGION_DATA.keys()).index(st.session_state.current_region),
        horizontal=True,
        label_visibility="collapsed"
    )
    st.session_state.current_region = region_choice
    region_info = REGION_DATA[region_choice]

    for theme, theme_label in region_info["themes"].items():
        theme_courses = [c for c in region_info["courses"] if c["theme"] == theme]
        if not theme_courses:
            continue
        st.markdown(f"### {theme_label}")
        cols = st.columns(min(len(theme_courses), 3))
        for i, course in enumerate(theme_courses):
            with cols[i % 3]:
                diff_color = {"Easy": DIFF_EASY, "Moderate": DIFF_MODERATE, "Challenge": DIFF_CHALLENGE}[course['difficulty']]
                pet_icon = "🐾" if course['pet_friendly'] else ""
                st.markdown(
                    f"<div style='background:white;border-radius:12px;padding:16px;"
                    f"border:1px solid {CARD_BORDER};margin-bottom:8px;"
                    f"box-shadow:0 2px 8px rgba(0,0,0,0.06);min-height:140px'>"
                    f"<div style='font-weight:700;color:{CARD_VALUE};margin-bottom:6px'>{course['name_en']}</div>"
                    f"<div style='font-size:0.82rem;color:{TEXT_MUTED_ALT};margin-bottom:10px'>{course['description_en'][:80]}...</div>"
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
                    st.session_state.current_region = region_choice
                    st.session_state.route = None
                    st.session_state.descriptions = {}
                    st.session_state.restaurants = None
                    st.session_state.accommodations = None
                    st.rerun()
        st.markdown("")