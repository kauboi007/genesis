from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="AXION Core API")

# ---------- MODELS ----------
class HealthData(BaseModel):
    age: int
    heart_rate: float
    sleep_hours: float
    stress_level: float

class FinanceData(BaseModel):
    income: float
    expenses: float
    investments: float
    credit_score: int

class BehaviorData(BaseModel):
    focus_level: float
    fatigue_level: float
    mood_score: float

# ---------- ENDPOINTS ----------
@app.get("/")
def home():
    return {"msg": "AXION Central Core running successfully"}

@app.post("/predict_health")
def predict_health(data: HealthData) -> Dict[str, float]:
    score = 100 - (data.stress_level * 10) + (data.sleep_hours * 2)
    score = max(0, min(score, 100))
    return {"health_score": round(score, 2)}

@app.post("/predict_finance")
def predict_finance(data: FinanceData) -> Dict[str, float]:
    balance = data.income - data.expenses + (data.investments * 0.05)
    risk_factor = (700 - data.credit_score) / 10
    score = max(0, min(100, (balance / 1000) - risk_factor))
    return {"finance_health": round(score, 2)}

@app.post("/behavior_map")
def behavior_map(data: BehaviorData) -> Dict[str, float]:
    performance = (data.focus_level * 1.5) - (data.fatigue_level * 0.7) + (data.mood_score * 1.2)
    score = max(0, min(100, performance * 10))
    return {"behavior_index": round(score, 2)}

