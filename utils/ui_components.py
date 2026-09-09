import streamlit as st
from api.tour_api import format_place

def inject_course_finder_css():
    """Injects the custom CSS for the Course Finder page."""
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

def render_course_detail(course):
    """Renders the detailed view of a selected course."""
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

def render_nearby_spots(course, restaurants, accommodations):
    """Renders the nearby restaurants and accommodations section."""
    st.markdown("### 🍽️ After Your Plogging")
    st.caption("Nearby spots powered by 한국관광공사 OpenAPI")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🍜 Nearby Restaurants")
        if restaurants:
            for r in restaurants[:4]:
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
        if accommodations:
            for a in accommodations[:4]:
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

# UI Color Constants
CARD_BORDER = "#D4C9B8"
CARD_VALUE = "#2D6A4F"
TEXT_MUTED_ALT = "#666666"

# Button Colors
BTN_PRIMARY = "#2D6A4F"
BTN_SECONDARY = "#0066CC"
BTN_TERTIARY = "#40916C"

# Kakao Map Button
KAKAO_BG = "#FEE500"
KAKAO_TEXT = "#3C1E1E"

# Difficulty Colors
DIFF_EASY = "#2D6A4F"
DIFF_MODERATE = "#856404"
DIFF_CHALLENGE = "#842029"
TEXT_MUTED = '#888888'
