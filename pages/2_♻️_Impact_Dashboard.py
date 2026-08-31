import streamlit as st
import pandas as pd
from datetime import date
from supabase import create_client
import os
from dotenv import load_dotenv
from utils.jeju_olle import JEJU_OLLE_COURSES

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

st.set_page_config(page_title="Impact Dashboard", page_icon="♻️", layout="wide")

st.title("♻️ Plogging Impact Dashboard")
st.subheader("Track your contribution to a cleaner Korea")

# ── 기록 입력 ──
st.markdown("### 📝 Log Your Session")
col1, col2, col3, col4 = st.columns(4)

with col1:
    log_date = st.date_input("Date", value=date.today())
with col2:
    course_options = [c["name_en"] for c in JEJU_OLLE_COURSES]
    course_name = st.selectbox("Course", course_options)
with col3:
    waste_kg = st.number_input("Waste collected (kg)", min_value=0.1, max_value=50.0, value=0.5, step=0.1)
with col4:
    distance_km = st.number_input("Distance jogged (km)", min_value=0.1, max_value=50.0, value=3.0, step=0.1)

waste_type = st.multiselect(
    "Type of waste collected",
    ["Plastic bottles", "Food packaging", "Cigarette butts", "Glass", "Paper", "Metal cans", "Styrofoam", "Other"],
    default=["Plastic bottles", "Food packaging"]
)

if st.button("➕ Log This Session", type="primary"):
    try:
        supabase.table("plogging_logs").insert({
            "date": str(log_date),
            "course": course_name,
            "waste_kg": waste_kg,
            "distance_km": distance_km,
            "waste_types": ", ".join(waste_type)
        }).execute()
        st.success(f"✅ Logged! You collected {waste_kg}kg on {course_name}!")
        st.balloons()
    except Exception as e:
        st.error(f"Failed to save: {e}")

st.markdown("---")

# ── 데이터 로드 ──
try:
    response = supabase.table("plogging_logs").select("*").execute()
    all_data = response.data
except:
    all_data = []

DEMO_DATA = [
    {"date": "2026-08-01", "course": "Olle Route 1 ⭐ Best", "waste_kg": 1.2, "distance_km": 15.1, "waste_types": "Plastic bottles, Food packaging"},
    {"date": "2026-08-05", "course": "Olle Route 6 ⭐ Oedolgae", "waste_kg": 0.8, "distance_km": 11.0, "waste_types": "Cigarette butts, Plastic bottles"},
    {"date": "2026-08-10", "course": "Olle Route 9 ⭐ Sanbangsan", "waste_kg": 0.5, "distance_km": 8.4, "waste_types": "Food packaging, Styrofoam"},
    {"date": "2026-08-15", "course": "Olle Route 14 ⭐ Hyeopjae", "waste_kg": 2.1, "distance_km": 19.5, "waste_types": "Plastic bottles, Metal cans"},
    {"date": "2026-08-20", "course": "Olle Route 21 ⭐ Jimibong", "waste_kg": 0.9, "distance_km": 11.7, "waste_types": "Cigarette butts, Food packaging"},
]

display_data = all_data if all_data else DEMO_DATA
df = pd.DataFrame(display_data)

# ── 누적 통계 ──
st.markdown("### 🌍 Global Impact (All Participants)")
total_waste = df["waste_kg"].sum()
total_distance = df["distance_km"].sum()
total_sessions = len(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Waste Collected", f"{total_waste:.1f} kg")
col2.metric("Total Distance Jogged", f"{total_distance:.1f} km")
col3.metric("Total Sessions", f"{total_sessions}")
col4.metric("Avg per Session", f"{total_waste/total_sessions:.2f} kg")

st.markdown("---")

# ── 차트 ──
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📈 Waste Collected Over Time")
    chart_df = df[["date", "waste_kg"]].copy()
    chart_df = chart_df.sort_values("date")
    chart_df["cumulative_kg"] = chart_df["waste_kg"].cumsum()
    st.line_chart(chart_df.set_index("date")["cumulative_kg"])

with col2:
    st.markdown("### 🗺️ Top Courses by Impact")
    course_df = df.groupby("course")["waste_kg"].sum().sort_values(ascending=False).reset_index()
    course_df.columns = ["Course", "Waste (kg)"]
    st.bar_chart(course_df.set_index("Course"))

st.markdown("---")

# ── 전체 로그 ──
st.markdown("### 🏅 All Sessions")
if all_data:
    log_df = pd.DataFrame(all_data)[["date", "course", "waste_kg", "distance_km", "waste_types"]]
    st.dataframe(log_df, use_container_width=True)
else:
    st.info("No real sessions yet. Be the first to log your plogging! 🏃")

st.markdown("---")

# ── 환경 임팩트 환산 ──
st.markdown("### 🌱 What Your Impact Means")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🌳 Equivalent trees saved", f"{total_waste * 0.5:.0f}")
with col2:
    st.metric("🍶 Plastic bottles removed", f"{int(total_waste / 0.025):,}")
with col3:
    st.metric("💨 CO₂ equivalent reduced (kg)", f"{total_waste * 2.5:.1f}")

st.markdown("---")
st.caption("Real data stored in Supabase. Demo data shown when no sessions logged yet.")