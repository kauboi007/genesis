import streamlit as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(page_title="FINESIGHT | Genesis 5.0", layout="centered")

st.title("💰 FINESIGHT — Financial Intelligence Engine")
st.caption("Assess your financial stability and discover personalized investment recommendations.")

# --- Input Fields ---
income = st.number_input("Monthly Income (₹)", 0.0, 1000000.0, 50000.0)
expenses = st.number_input("Monthly Expenses (₹)", 0.0, 1000000.0, 30000.0)
savings = st.number_input("Current Savings (₹)", 0.0, 10000000.0, 150000.0)
credit_score = st.slider("Credit Score", 300, 900, 700)
market_sentiment = st.slider("Market Sentiment (-10 = Bearish, +10 = Bullish)", -10, 10, 2)

# ✅ Changed name here — now shows as Investment Risk Tolerance
risk_tolerance = st.slider("Investment Risk Tolerance (1 = Low, 10 = High)", 1, 10, 5)

if st.button("🔍 Analyze Finance"):
    with st.spinner("Evaluating financial health..."):
        payload = {
            "income": income,
            "expenses": expenses,
            "savings": savings,
            "credit_score": credit_score,
            "market_sentiment": market_sentiment,
            "risk_tolerance": risk_tolerance
        }

        try:
            resp = requests.post("http://127.0.0.1:8002/predict_finance", json=payload, timeout=6)
            data = resp.json()

            if "error" in data:
                st.error(data["error"])
            else:
                st.success(f"✅ Analysis Complete — Risk Profile: **{data['risk_profile']}**")
                st.metric("Financial Health", f"{data['financial_health']:.2f}/100")

                st.markdown("### 📊 Recommended Investment Portfolio")
                plan = data.get("investment_plan", {})
                if plan:
                    labels = list(plan.keys())
                    values = list(plan.values())
                    fig, ax = plt.subplots()
                    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
                    ax.axis("equal")
                    st.pyplot(fig)

                st.info(f"💡 {data['advice']}")

                # --- 🧭 Personalized Investment Suggestions ---
                st.markdown("### 🧠 Personalized Investment Suggestions")

                suggestions = []
                if risk_tolerance <= 3:
                    suggestions = ["Fixed Deposits", "Government Bonds", "Index Funds"]
                elif risk_tolerance <= 6:
                    suggestions = ["Balanced Mutual Funds", "Blue-Chip Stocks", "Gold ETFs"]
                else:
                    suggestions = ["Equity Mutual Funds", "High-Growth Stocks", "Cryptocurrency (small %)"]

                if market_sentiment < -3:
                    st.warning("📉 Current market is bearish — consider defensive investments.")
                elif market_sentiment > 3:
                    st.success("📈 Bullish market detected — potential for short-term growth opportunities.")

                st.write(f"Based on your risk level ({risk_tolerance}/10) and market sentiment, you can explore:")
                for s in suggestions:
                    st.write(f"- 💹 **{s}**")

                if savings < expenses * 3:
                    st.warning("⚠️ Your savings cover less than 3 months of expenses — build an emergency fund first.")
                elif savings > income * 6:
                    st.success("💰 Strong savings — consider diversifying into higher-yield investments.")

        except Exception as e:
            st.error(f"Error connecting to FINESIGHT Core: {e}")