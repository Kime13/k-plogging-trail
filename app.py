import streamlit as st

st.set_page_config(page_title="K-Plogging Trail", page_icon="🌿", layout="wide")

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