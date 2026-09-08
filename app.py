import streamlit as st

st.set_page_config(page_title="K-Plogging Trail", page_icon="🌿", layout="wide")

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #E8F5E9 0%, #B2DFDB 40%, #C8E6C9 100%); }
    [data-testid="stSidebar"] { display: none; }
    header { display: none; }

    .landing-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 90vh;
        padding: 40px 20px;
    }

    .hero-card {
        background: linear-gradient(145deg, #ffffff 0%, #f0faf0 50%, #e0f5e8 100%);
        border-radius: 40px;
        width: 500px;
        height: 500px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 20px 60px rgba(46,125,50,0.18), 0 4px 20px rgba(46,125,50,0.1);
        border: 1.5px solid rgba(129,199,132,0.4);
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .hero-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 32px 80px rgba(46,125,50,0.25);
    }

    .hero-card::before {
        content: '';
        position: absolute;
        top: -50px; right: -50px;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(129,199,132,0.3), transparent 70%);
        border-radius: 50%;
    }

    .hero-card::after {
        content: '';
        position: absolute;
        bottom: -70px; left: -40px;
        width: 250px; height: 250px;
        background: radial-gradient(circle, rgba(77,182,172,0.2), transparent 70%);
        border-radius: 50%;
    }

    .icon-wrap {
        width: 96px; height: 96px;
        background: linear-gradient(135deg, #43A047, #2E7D32);
        border-radius: 28px;
        display: flex; align-items: center; justify-content: center;
        font-size: 50px;
        box-shadow: 0 8px 24px rgba(46,125,50,0.35);
        margin-bottom: 24px;
        z-index: 1;
    }

    .hero-title {
        color: #1B5E20;
        font-size: 2.2rem;
        font-weight: 800;
        text-align: center;
        margin: 0 0 10px 0;
        z-index: 1;
        letter-spacing: -0.5px;
    }

    .hero-subtitle {
        color: #4CAF50;
        font-size: 1rem;
        font-style: italic;
        text-align: center;
        margin: 0 0 24px 0;
        z-index: 1;
    }

    .hero-badge {
        background: linear-gradient(135deg, #E8F5E9, #C8E6C9);
        border: 1.5px solid rgba(76,175,80,0.4);
        border-radius: 24px;
        padding: 10px 22px;
        color: #2E7D32;
        font-size: 0.85rem;
        font-weight: 600;
        z-index: 1;
        box-shadow: 0 2px 8px rgba(76,175,80,0.15);
    }

    .tap-hint {
        margin-top: 28px;
        color: #558B2F;
        font-size: 0.82rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        opacity: 0.7;
        animation: pulse 2.5s ease-in-out infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 0.5; transform: translateY(0); }
        50% { opacity: 0.9; transform: translateY(-4px); }
    }

    .dots {
        display: flex; gap: 8px; margin-top: 16px; align-items: center;
    }
    .dot {
        width: 8px; height: 8px;
        border-radius: 50%;
        background: rgba(46,125,50,0.25);
    }
    .dot.active {
        width: 28px; border-radius: 4px;
        background: #43A047;
    }

    /* 버튼 숨기기 */
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
    <div class='landing-wrapper'>
        <div class='hero-card'>
            <div class='icon-wrap'>🌿</div>
            <p class='hero-title'>K-Plogging Trail</p>
            <p class='hero-subtitle'>Making your journey more enjoyable</p>
            <div class='hero-badge'>🏃 Run &nbsp;·&nbsp; ♻️ Pick &nbsp;·&nbsp; 🌍 Make Korea Cleaner</div>
        </div>
        <p class='tap-hint'>↑ Tap to explore</p>
        <div class='dots'>
            <div class='dot active'></div>
            <div class='dot'></div>
            <div class='dot'></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 투명 버튼으로 전체 화면 클릭 감지
    if st.button("enter", key="enter_btn"):
        st.session_state.entered = True
        # fade out 애니메이션 후 전환
        st.markdown("""
        <style>
        .landing-wrapper {
            animation: fadeOut 0.6s ease forwards !important;
        }
        @keyframes fadeOut {
            0% { opacity: 1; transform: scale(1); }
            100% { opacity: 0; transform: scale(1.05); }
        }
        </style>
        """, unsafe_allow_html=True)
        import time
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