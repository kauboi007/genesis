import streamlit as st
import requests
import time

st.set_page_config(page_title="SYNAPSE – Behavioral AI", layout="centered")

st.title("🧠 SYNAPSE – Behavioral & Productivity Intelligence")
st.write("Analyze your emotional and cognitive patterns to boost focus and wellbeing.")

# --- Inputs ---
mood_level = st.slider("😊 Current Mood Level (1 = Low, 10 = Great)", 1.0, 10.0, 7.0)
sleep_hours = st.slider("🛌 Sleep Duration (hours)", 3.0, 10.0, 7.0)
focus_hours = st.slider("🎯 Productive Focus Hours (per day)", 1.0, 12.0, 6.0)
distractions = st.slider("📱 Distractions per Hour", 0.0, 10.0, 3.0)
caffeine_intake = st.slider("☕ Caffeine Intake (cups per day)", 0.0, 6.0, 2.0)
screen_time = st.slider("💻 Screen Time (hours per day)", 1.0, 14.0, 8.0)
stress_level = st.slider("😣 Stress Level (1 = Low, 10 = High)", 1.0, 10.0, 5.0)

if st.button("🔍 Analyze My Cognitive State"):
    with st.spinner("Fetching data from Aura and Axion modules..."):
        time.sleep(1.5)
        try:
            res = requests.post("http://127.0.0.1:8003/predict_behavior", json={
                "mood_level": mood_level,
                "sleep_hours": sleep_hours,
                "focus_hours": focus_hours,
                "distractions": distractions,
                "caffeine_intake": caffeine_intake,
                "screen_time": screen_time,
                "stress_level": stress_level
            })
            result = res.json()

            st.success(f"🧩 Focus-Productivity Score: **{result['focus_score']:.2f}/100**")
            st.subheader("🧭 Summary")
            st.info(result["summary"])

            st.subheader("💡 Personalized Recommendations:")
            for tip in result["advice"]:
                st.markdown(f"✅ {tip}")

        except Exception as e:
            st.error(f"Error: {e}")
