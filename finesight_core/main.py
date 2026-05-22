from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI(title="FINESIGHT Core", version="2.0")

class FinanceInput(BaseModel):
    income: float
    expenses: float
    savings: float
    credit_score: float
    market_sentiment: float
    risk_tolerance: float  # new field name

@app.post("/predict_finance")
def predict_finance(data: FinanceInput):
    try:
        # --- Basic Financial Health Calculation ---
        savings_rate = (data.savings / max(data.income, 1)) * 100
        expense_ratio = (data.expenses / max(data.income, 1)) * 100
        credit_factor = (data.credit_score - 300) / 600  # normalize 0–1
        market_factor = (data.market_sentiment + 10) / 20  # normalize -10–10 → 0–1
        risk_factor = data.risk_tolerance / 10

        # Weighted heuristic score (0–100)
        financial_health = round(
            (0.3 * savings_rate + 0.2 * (100 - expense_ratio) +
             0.3 * (credit_factor * 100) + 0.2 * (market_factor * 100)) * (0.7 + 0.3 * risk_factor), 2
        )

        financial_health = min(max(financial_health, 0), 100)

        # --- Investment Suggestion Logic ---
        if risk_factor < 0.3:
            plan = {
                "Fixed Deposits": 40,
                "Government Bonds": 30,
                "Index Funds": 20,
                "Gold ETFs": 10
            }
            risk_profile = "Conservative"
        elif risk_factor < 0.7:
            plan = {
                "Balanced Mutual Funds": 30,
                "Blue-chip Stocks": 30,
                "Bonds": 20,
                "REITs": 10,
                "Cash Reserve": 10
            }
            risk_profile = "Moderate"
        else:
            plan = {
                "Equity Stocks": 40,
                "Tech/Crypto ETFs": 25,
                "International Funds": 20,
                "Startups/Alt": 10,
                "Cash": 5
            }
            risk_profile = "Aggressive"

        # --- Advice ---
        advice = f"Based on your {risk_profile} risk profile, diversify investments as suggested."

        return {
            "financial_health": financial_health,
            "risk_profile": risk_profile,
            "investment_plan": plan,
            "advice": advice
        }

    except Exception as e:
        return {"error": str(e)}