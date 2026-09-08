import streamlit as st
import time

st.set_page_config(page_title="K-Plogging Trail", page_icon="🌿", layout="wide")

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(160deg, #e8f5e9 0%, #c8e6c9 40%, #b2dfdb 100%);
    }
    [data-testid="stSidebar"] { display: none; }
    header { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    .landing {
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 24px;
        padding: 40px 20px;
    }

    .hero-card {
        width: 460px;
        height: 460px;
        background: white;
        border-radius: 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 20px 60px rgba(46,125,50,0.15), 0 4px 16px rgba(46,125,50,0.08);
        border: 1.5px solid rgba(129,199,132,0.35);
        position: relative;
        overflow: hidden;
        transition: transform 0.35s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.35s ease, opacity 0.5s ease;
        cursor: pointer;
    }
    .hero-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 32px 80px rgba(46,125,50,0.22), 0 8px 24px rgba(46,125,50,0.12);
    }
    .hero-card:active {
        transform: scale(0.98);
    }
    .hero-card.fade-out {
        opacity: 0;
        transform: scale(1.04);
    }
    .hero-card::before {
        content: '';
        position: absolute;
        top: -40px; right: -40px;
        width: 160px; height: 160px;
        background: radial-gradient(circle, rgba(165,214,167,0.4), transparent 70%);
        border-radius: 50%;
    }
    .hero-card::after {
        content: '';
        position: absolute;
        bottom: -60px; left: -30px;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(77,182,172,0.2), transparent 70%);
        border-radius: 50%;
    }

    .icon-wrap {
        width: 88px; height: 88px;
        background: linear-gradient(135deg, #43a047, #2e7d32);
        border-radius: 24px;
        display: flex; align-items: center; justify-content: center;
        font-size: 44px;
        box-shadow: 0 8px 24px rgba(46,125,50,0.3);
        margin-bottom: 22px;
        z-index: 1;
        transition: transform 0.3s ease;
    }
    .hero-card:hover .icon-wrap {
        transform: rotate(-5deg) scale(1.08);
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 800;
        color: #1b5e20;
        margin: 0 0 8px;
        text-align: center;
        letter-spacing: -0.5px;
        z-index: 1;
    }
    .hero-subtitle {
        font-size: 0.95rem;
        color: #4caf50;
        font-style: italic;
        margin: 0 0 22px;
        text-align: center;
        z-index: 1;
    }
    .hero-badge {
        background: linear-gradient(135deg, #e8f5e9, #c8e6c9);
        border: 1.5px solid rgba(76,175,80,0.4);
        border-radius: 24px;
        padding: 9px 20px;
        font-size: 0.82rem;
        color: #2e7d32;
        font-weight: 600;
        z-index: 1;
        letter-spacing: 0.3px;
    }
    .hero-hint {
        font-size: 0.78rem;
        color: rgba(46,125,50,0.5);
        margin: 18px 0 0;
        z-index: 1;
        letter-spacing: 0.5px;
    }

    .dots {
        display: flex; gap: 8px; align-items: center;
    }
    .dot-active {
        width: 28px; height: 8px;
        border-radius: 4px;
        background: #43a047;
    }
    .dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: rgba(46,125,50,0.25);
    }
    .powered {
        font-size: 0.72rem;
        color: rgba(46,125,50,0.45);
        letter-spacing: 0.5px;
    }

    /* 투명 버튼으로 전체 클릭 감지 */
    .stButton > button {
        position: fixed !important;
        top: 0 !important; left: 0 !important;
        width: 100vw !important; height: 100vh !important;
        opacity: 0 !important;
        cursor: pointer !important;
        z-index: 999 !important;
        border: none !important;
        background: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='landing'>
        <div class='hero-card' id='heroCard'>
            <div class='icon-wrap'>🌿</div>
            <p class='hero-title'>K-Plogging Trail</p>
            <p class='hero-subtitle'>Making your journey more enjoyable</p>
            <div class='hero-badge'>🏃 Run &nbsp;·&nbsp; ♻️ Pick &nbsp;·&nbsp; 🌍 Make Korea Cleaner</div>
            <p class='hero-hint'>Tap anywhere to enter</p>
        </div>
        <div class='dots'>
            <div class='dot-active'></div>
            <div class='dot'></div>
            <div class='dot'></div>
        </div>
        <p class='powered'>Powered by 한국관광공사 OpenAPI × WanderRabbit 🐰</p>
    </div>

    <script>
    document.getElementById('heroCard').addEventListener('click', function() {
        this.classList.add('fade-out');
    });
    </script>
    """, unsafe_allow_html=True)

    if st.button("enter", key="enter_btn"):
        st.session_state.entered = True
        time.sleep(0.5)
        st.rerun()

else:
    st.markdown("""
    <style>
    .stApp { background-color: #F7F3EE; }
    </style>
    """, unsafe_allow_html=True)

    st.title("🌿 K-Plogging Trail")
    st.subheader("Run. Pick. Make Korea Cleaner.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🗺️ Course Finder")
        st.write("Browse plogging courses in Jeju, Seoul, and Busan — filtered by difficulty, theme, and pet-friendliness.")
        st.page_link("pages/1_🗺️_Course_Finder.py", label="Find a Course →")
    with col2:
        st.markdown("### ♻️ Impact Dashboard")
        st.write("Log your plogging sessions and see your contribution to a cleaner Korea.")
        st.page_link("pages/2_♻️_Impact_Dashboard.py", label="Log My Impact →")
    with col3:
        st.markdown("### 🌍 Why Plogging?")
        st.write("Plogging = Jogging + Picking up trash. Join the global eco-fitness movement in Korea.")
        st.info("1 session = ~1kg of waste removed from nature")

    st.markdown("---")
    st.markdown("**Powered by** 한국관광공사 OpenAPI × Gemini AI × Kakao Maps × WanderRabbit 🐰")