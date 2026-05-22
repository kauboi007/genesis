# genesis_fusion/fusion_dashboard.py
import streamlit as st
import requests
import time
import math
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="GENESIS", layout="centered")


from PIL import Image

# Load and display logo safely in Streamlit
logo_path = "C:/Users/123co/OneDrive/Documents/Genesis5.0/Black and White Monochrome Tech Logo.png"

try:
    logo_img = Image.open(logo_path)
    st.markdown("<div style='display: flex; justify-content: center; align-items: center;'>", unsafe_allow_html=True)
    st.image(logo_img, width=150)
    st.markdown("</div>", unsafe_allow_html=True)
except Exception as e:
    st.warning(f"⚠️ Logo not found or couldn't be loaded: {e}")

# Title and tagline (centered)
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="margin-bottom: 0;">GENESIS 5.0</h1>
        <p style="color: gray; font-size: 20px;">The Unified Life Intelligence System.</p>
    </div>
    """,
    unsafe_allow_html=True
)





col1, col2 = st.columns(2)
with col1:
    st.subheader("AURA inputs (Health)")
    age = st.number_input("Age", 15, 100, 28)
    heart_rate = st.number_input("Heart rate (bpm)", 40, 120, 72)
    sleep_hours = st.slider("Sleep hours", 0.0, 12.0, 7.0)
    activity_level = st.slider("Activity level (1-10)", 1, 10, 6)
    stress_level = st.slider("Stress (1-10)", 1, 10, 4)
    diet_quality = st.slider("Diet (1-10)", 1, 10, 7)

with col2:
    st.subheader("FINESIGHT inputs (Finance)")
    income = st.number_input("Monthly income", 0.0, 1_000_000.0, 50000.0)
    expenses = st.number_input("Monthly expenses", 0.0, 1_000_000.0, 30000.0)
    savings = st.number_input("Current savings", 0.0, 5_000_000.0, 15000.0)
    credit_score = st.slider("Credit score (300-900)", 300, 900, 700)
    market_sentiment = st.slider("Market sentiment (-10 to +10)", -10, 10, 2)
    online_risk_activity = st.slider("Online risk behavior (1-10)", 1, 10, 3)

st.markdown("---")
st.subheader("SYNAPSE inputs (Behavior)")
focus_hours = st.slider("Focus hours (per day)", 0.0, 12.0, 5.0)
fatigue_level = st.slider("Fatigue (1-10)", 1.0, 10.0, 3.0)
mood_score = st.slider("Mood (1-10)", 1.0, 10.0, 7.0)
distractions = st.slider("Distractions per hour", 0.0, 20.0, 3.0)
caffeine = st.slider("Caffeine cups/day", 0.0, 10.0, 2.0)
screen_time = st.slider("Screen time (hrs/day)", 0.0, 20.0, 7.0)

st.markdown("---")
run = st.button("🚀 Generate Full Intelligence Report")

# helper UI placeholders
status_placeholder = st.empty()
progress = st.progress(0)
log_box = st.empty()

def update_progress(step, pct, msg):
    status_placeholder.info(f"**{step}** — {msg}")
    progress.progress(pct)
    log_box.text(msg)

def safe_post(url, payload, timeout=6):
    try:
        r = requests.post(url, json=payload, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        return {"error": str(e)}

if run:
    try:
        # Step 1: Query AURA service (port 8001)
        update_progress("1/5 — Querying AURA", 5, "Contacting AURA (health)")
        aura_payload = {
            "age": int(age),
            "heart_rate": float(heart_rate),
            "sleep_hours": float(sleep_hours),
            "activity_level": float(activity_level),
            "stress_level": float(stress_level),
            "diet_quality": float(diet_quality)
        }
        aura_resp = safe_post("http://127.0.0.1:8001/predict_health", aura_payload)
        time.sleep(0.7)

        # Step 2: Query FINESIGHT (port 8002)
        update_progress("2/5 — Querying FINESIGHT", 30, "Gathering financial & cyber signals")
        finesight_payload = {
            "income": float(income),
            "expenses": float(expenses),
            "savings": float(savings),
            "credit_score": float(credit_score),
            "market_sentiment": float(market_sentiment),
            "online_risk_activity": float(online_risk_activity)
        }
        fin_resp = safe_post("http://127.0.0.1:8002/predict_finance", finesight_payload)
        time.sleep(0.7)

        # Step 3: Query SYNAPSE (port 8003)
        update_progress("3/5 — Querying SYNAPSE", 55, "Analyzing cognitive & behavioral state")
        syn_payload = {
            "mood_level": float(mood_score),
            "sleep_hours": float(sleep_hours),
            "focus_hours": float(focus_hours),
            "distractions": float(distractions),
            "caffeine_intake": float(caffeine),
            "screen_time": float(screen_time),
            "stress_level": float(stress_level)
        }
        syn_resp = safe_post("http://127.0.0.1:8003/predict_behavior", syn_payload)
        time.sleep(0.7)

        # Validate responses and extract numeric scores (fall back if error)
        def extract_score(resp, key, fallback):
            if resp is None:
                return fallback, f"no response (fallback {fallback})"
            if "error" in resp:
                return fallback, resp["error"]
            if key in resp:
                try:
                    return float(resp[key]), None
                except:
                    return fallback, "parse-error"
            # try common keys
            for k in ["health_score", "financial_health", "finance_health", "focus_score", "behavior_index"]:
                if k in resp:
                    try:
                        return float(resp[k]), None
                    except:
                        pass
            return fallback, "unknown-response-format"

        aura_score, aura_err = extract_score(aura_resp, "health_score", 50.0)
        fin_score, fin_err = extract_score(fin_resp, "financial_health", 50.0)
        syn_score, syn_err = extract_score(syn_resp, "focus_score", 50.0)

        # Step 4: Fuse results
        update_progress("4/5 — Fusing results", 80, "Computing Life Intelligence Index (LII)")
        # weights customizable
        w_health, w_fin, w_syn = 0.4, 0.3, 0.3
        lii = round(aura_score * w_health + fin_score * w_fin + syn_score * w_syn, 2)

        # Build combined advice (merge module advices if present)
        adv_list = []
        if isinstance(aura_resp, dict) and "advice" in aura_resp:
            if isinstance(aura_resp["advice"], list):
                adv_list += aura_resp["advice"]
            else:
                adv_list.append(aura_resp["advice"])
        if isinstance(fin_resp, dict) and "advice" in fin_resp:
            if isinstance(fin_resp["advice"], list):
                adv_list += fin_resp["advice"]
            else:
                adv_list.append(fin_resp["advice"])
        if isinstance(syn_resp, dict) and "advice" in syn_resp:
            if isinstance(syn_resp["advice"], list):
                adv_list += syn_resp["advice"]
            else:
                adv_list.append(syn_resp["advice"])

        # Generate AXION-like recommendation (local rules)
        update_progress("5/5 — Generating AXION recommendation", 95, "Formulating prioritized action plan")
        time.sleep(0.6)

        # Decision language + short/medium/long plan
        if lii >= 80:
            decision = "Optimal — Maintain and monitor"
            short = "Keep current routine; 15-min light exercise today."
            medium = "Review investment allocations quarterly."
            long = "Sustainable plan: keep sleep, hydration; scale workouts."
        elif lii >= 60:
            decision = "Caution — Improve targeted areas"
            short = "Sleep + hydration tonight; avoid high-risk sites."
            medium = "Cut 10% discretionary spend; implement Pomodoro blocks."
            long = "Build 3-month plan: improve diet, emergency fund, stress therapy."
        else:
            decision = "Action Required — Immediate intervention"
            short = "Take a 24–48 hour rest window; reduce screen time."
            medium = "Schedule doctor/financial counselor; freeze risky transactions."
            long = "Commit to a 6-month wellbeing + budget recovery plan."

        # Finalize progress
        update_progress("Complete", 100, "Report ready")

        # ---- Display results ----
        st.markdown("## 🔎 Module Results")
        cols = st.columns(3)
        cols[0].metric("🩺 Health Score (AURA)", f"{aura_score:.2f}", "source: AURA")
        cols[1].metric("💰 Finance Health (FINESIGHT)", f"{fin_score:.2f}", "source: FINESIGHT")
        cols[2].metric("🧠 Focus Index (SYNAPSE)", f"{syn_score:.2f}", "source: SYNAPSE")

        st.markdown("---")
        st.subheader("🌟 Life Intelligence Index (LII)")
        st.metric("LII (0–100)", f"{lii:.2f}")

        st.markdown("### 🧠 AXION Recommendation")
        st.info(f"**{decision}**")
        st.write("**Short-term:**", short)
        st.write("**Medium-term:**", medium)
        st.write("**Long-term:**", long)

        if adv_list:
            st.markdown("---")
            st.subheader("🔧 Collected module tips (merged)")
            for tip in adv_list:
                st.markdown(f"- {tip}")

        # ---- Single comparative chart (matplotlib) ----
        st.markdown("---")
        st.subheader("📊 Summary Chart")
        labels = ["Health", "Finance", "Behavior", "LII"]
        values = [aura_score, fin_score, syn_score, lii]

        fig, ax = plt.subplots(figsize=(6, 3.5))
        x = np.arange(len(labels))
        colors = ["#E74C3C", "#27AE60", "#3498DB", "#F804C7"]  # red, green, blue, purple (for LII)
        ax.bar(x, values, color=colors)
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylim(0, 100)
        ax.set_ylabel("Score (0-100)")
        ax.set_title("Module Scores and Life Intelligence Index")
        st.pyplot(fig)

        st.success("✅ Full Intelligence Report generated successfully")

    except Exception as e:
        st.error(f"An error occurred during fusion: {e}")
        st.write("AURA response:", aura_resp)
        st.write("FINESIGHT response:", fin_resp)
        st.write("SYNAPSE response:", syn_resp)
