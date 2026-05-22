from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import uvicorn

app = FastAPI()

# --- Data model ---
class SynapseData(BaseModel):
    mood_level: float
    sleep_hours: float
    focus_hours: float
    distractions: float
    caffeine_intake: float
    screen_time: float
    stress_level: float

# --- ML training data ---
X = np.array([
    [8, 7, 6, 2, 2, 5, 3],
    [5, 5, 4, 6, 4, 8, 7],
    [9, 8, 8, 1, 1, 4, 2],
    [6, 6, 5, 4, 3, 6, 4],
    [3, 4, 3, 7, 5, 9, 8]
])
y = np.array([88, 55, 92, 70, 40])  # Focus-Productivity score (0–100)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

@app.post("/predict_behavior")
def predict_behavior(data: SynapseData):
    inp = np.array([[data.mood_level, data.sleep_hours, data.focus_hours, data.distractions,
                     data.caffeine_intake, data.screen_time, data.stress_level]])
    score = model.predict(inp)[0]
    score = float(np.clip(score, 0, 100))

    if score >= 80:
        summary = "Peak cognitive flow! You're highly productive and emotionally balanced."
        tips = [
            "Keep consistent sleep-wake cycles.",
            "Continue short mindful breaks to sustain focus.",
            "Maintain low caffeine for long-term balance."
        ]
    elif score >= 60:
        summary = "Moderate focus levels detected. Some fatigue or mild distraction."
        tips = [
            "Try 25-5 Pomodoro focus cycles.",
            "Take a 15-min outdoor break every 3 hours.",
            "Track your caffeine and hydration balance."
        ]
    else:
        summary = "Low behavioral stability. High stress or burnout indicators found."
        tips = [
            "Reduce screen exposure post 9 PM.",
            "Do short breathing exercises to lower cortisol.",
            "Prioritize 7+ hours of uninterrupted sleep."
        ]

    return {"focus_score": score, "summary": summary, "advice": tips}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8003)
