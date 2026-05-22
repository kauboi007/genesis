import streamlit as st
import requests

st.title("⚖️ AXION - Decision & Ethical Intelligence")

logic = st.slider("Logic Score (0-10)", 0, 10, 7)
emotion = st.slider("Emotion Score (0-10)", 0, 10, 5)

if st.button("Evaluate Decision"):
    res = requests.post("http://127.0.0.1:8000/decision_optimize",
                        json={"logic_score": logic, "emotion_score": emotion})
    data = res.json()
    st.metric("Rationality Index", data["rationality_index"])
    st.success(f"Decision Type: {data['status']}")
