import streamlit as st
import pandas as pd
from datetime import datetime, date

st.set_page_config(page_title="Impact Dashboard", page_icon="♻️", layout="wide")

st.title("♻️ Plogging Impact Dashboard")
st.subheader("Track your contribution to a cleaner Korea")

# session_state 초기화
if "plogging_logs" not in st.session_state:
    st.session_state.plogging_logs = []

# ── 기록 입력 ──
st.markdown("### 📝 Log Your Session")
col1, col2, col3, col4 = st.columns(4)

with col1:
    log_date = st.date_input("Date", value=date.today())
with col2:
    course_name = st.text_input("Course", placeholder="e.g. Olle Route 1")
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
    if course_name:
        st.session_state.plogging_logs.append({
            "date": str(log_date),
            "course": course_name,
            "waste_kg": waste_kg,
            "distance_km": distance_km,
            "waste_types": ", ".join(waste_type)
        })
        st.success(f"✅ Logged! You collected {waste_kg}kg on {course_name}!")
        st.balloons()
    else:
        st.warning("Please enter a course name.")

st.markdown("---")

# ── 더미 데이터 (데모용) ──
DEMO_DATA = [
    {"date": "2026-08-01", "course": "Olle Route 1", "waste_kg": 1.2, "distance_km": 15.1, "waste_types": "Plastic bottles, Food packaging"},
    {"date": "2026-08-05", "course": "Olle Route 6", "waste_kg": 0.8, "distance_km": 11.0, "waste_types": "Cigarette butts, Plastic bottles"},
    {"date": "2026-08-10", "course": "Olle Route 9", "waste_kg": 0.5, "distance_km": 8.4, "waste_types": "Food packaging, Styrofoam"},
    {"date": "2026-08-15", "course": "Olle Route 14", "waste_kg": 2.1, "distance_km": 19.5, "waste_types": "Plastic bottles, Metal cans, Glass"},
    {"date": "2026-08-20", "course": "Olle Route 21", "waste_kg": 0.9, "distance_km": 11.7, "waste_types": "Cigarette butts, Food packaging"},
]

all_logs = DEMO_DATA + st.session_state.plogging_logs
df = pd.DataFrame(all_logs)

# ── 누적 통계 ──
st.markdown("### 🌍 Global Impact (All Participants)")
total_waste = df["waste_kg"].sum()
total_distance = df["distance_km"].sum()
total_sessions = len(df)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Waste Collected", f"{total_waste:.1f} kg", delta=f"+{st.session_state.plogging_logs[-1]['waste_kg'] if st.session_state.plogging_logs else 0} kg today")
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

# ── 내 기록 ──
st.markdown("### 🏅 My Sessions")
if st.session_state.plogging_logs:
    my_df = pd.DataFrame(st.session_state.plogging_logs)
    my_waste = my_df["waste_kg"].sum()
    my_distance = my_df["distance_km"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("My Total Waste", f"{my_waste:.1f} kg")
    col2.metric("My Total Distance", f"{my_distance:.1f} km")
    col3.metric("My Sessions", len(st.session_state.plogging_logs))

    st.dataframe(my_df, use_container_width=True)

    # 기여도
    contribution_pct = (my_waste / total_waste) * 100
    st.progress(min(contribution_pct/100, 1.0))
    st.caption(f"Your contribution: {contribution_pct:.1f}% of all waste collected")
else:
    st.info("No personal sessions yet. Log your first plogging session above! 🏃")

st.markdown("---")

# ── 환경 임팩트 환산 ──
st.markdown("### 🌱 What Your Impact Means")
col1, col2, col3 = st.columns(3)
with col1:
    trees = total_waste * 0.5
    st.metric("🌳 Equivalent trees saved", f"{trees:.0f}")
with col2:
    plastic_bottles = int(total_waste / 0.025)
    st.metric("🍶 Plastic bottles removed", f"{plastic_bottles:,}")
with col3:
    co2_kg = total_waste * 2.5
    st.metric("💨 CO₂ equivalent reduced (kg)", f"{co2_kg:.1f}")

st.markdown("---")
st.markdown("*Demo data included for visualization. Real data accumulates as users log sessions.*")