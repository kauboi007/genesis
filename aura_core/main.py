from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class AuraData(BaseModel):
    sleep_hours: float
    activity_level: float
    stress_level: float
    diet_quality: float

@app.post("/predict_health")
def predict_health(data: AuraData):
    # prediction logic here
    return {"health_score": 0.85}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
