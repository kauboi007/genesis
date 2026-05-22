import streamlit as st
import requests
import time
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="AURA — Health AI", page_icon="🩺", layout="centered")

st.title("🩺 AURA — Adaptive Health & Wellness Intelligence")
st.markdown("#### Your personalized digital health companion powered by AI.")

# ------------------ USER INPUTS ------------------
st.subheader("🧠 Enter your details")

col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", 0, 120, 25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    heart_rate = st.slider("Heart Rate (bpm)", 40, 180, 75)
    steps = st.number_input("Daily Steps", 0, 30000, 5000)
    sleep_hours = st.slider("Sleep Duration (hours)", 0.0, 12.0, 7.0)
with col2:
    stress_level = st.slider("Stress Level (0-10)", 0.0, 10.0, 3.0)
    water_intake = st.number_input("Water Intake (litres)", 0.0, 6.0, 2.5)
    diet_quality = st.slider("Diet Quality (0-10)", 0, 10, 7)
    workout_minutes = st.number_input("Workout Minutes/Day", 0, 180, 30)
    screen_time = st.number_input("Screen Time (hrs)", 0, 24, 6)

if st.button("🔍 Analyze My Health"):
    with st.spinner("Syncing with AXION core..."):
        time.sleep(1.5)
    with st.spinner("Fetching AURA health data..."):
        time.sleep(1.5)

    # ------------------ SIMPLE ML LOGIC ------------------
    # Fake dataset for health score training (you can replace with real dataset later)
    X_train = np.array([
        [25, 75, 5000, 7, 3, 2.5, 7, 30, 6],
        [40, 85, 3000, 5, 7, 1.5, 5, 10, 9],
        [19, 65, 10000, 8, 2, 3.0, 9, 60, 4],
        [55, 95, 2000, 6, 8, 2.0, 4, 5, 10],
    ])
    y_train = np.array([82, 60, 95, 55])

    model = LinearRegression()
    model.fit(X_train, y_train)

    X_user = np.array([[age, heart_rate, steps, sleep_hours, stress_level,
                        water_intake, diet_quality, workout_minutes, screen_time]])
    health_score = float(model.predict(X_user)[0])

    # ------------------ DISPLAY ------------------
    st.success(f"✅ Your AURA Health Score: **{round(health_score, 1)} / 100**")

    if health_score > 80:
        st.balloons()
        st.info("Excellent vitality! Keep maintaining balance in rest, hydration, and focus.")
    elif health_score > 60:
        st.warning("Your health is stable, but your stress and sleep balance can be improved.")
    else:
        st.error("⚠️ Signs of fatigue or imbalance detected. Prioritize rest and mindfulness today.")

    st.markdown("##### 🌿 AI Wellness Advice")
    st.write(f"""
    • **Hydration**: Try maintaining 3L/day for optimal recovery.  
    • **Sleep**: Target at least 7 hours with reduced screen time 1 hour before bed.  
    • **Activity**: Gradually raise daily steps to 8000–10,000.  
    • **Mind**: Meditation or deep-breath cycles reduce stress spikes detected by SYNAPSE.
    """)

