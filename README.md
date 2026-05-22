# GENESIS 5.0 — Unified Life Intelligence System

## 🚀 Overview

**GENESIS 5.0** is an AI-powered life intelligence ecosystem that combines:

* 🩺 Health analysis
* 💰 Financial intelligence
* 🧠 Behavioral & productivity tracking
* ⚖️ Ethical decision optimization

into a single unified decision engine.

Instead of treating life domains separately, GENESIS fuses them into one intelligent system that generates a **Life Intelligence Index (LII)** and actionable recommendations.

Think of it as a personal operating system for your life.

---

## 🧠 Core Architecture

GENESIS is built using modular AI microservices:

| Module             | Purpose                                           |
| ------------------ | ------------------------------------------------- |
| **AURA**           | Health & wellness intelligence                    |
| **FINESIGHT**      | Financial health & investment analysis            |
| **SYNAPSE**        | Cognitive behavior & productivity prediction      |
| **AXION**          | Ethical and rational decision intelligence        |
| **GENESIS Fusion** | Combines all systems into one intelligence engine |

---

## ⚙️ Tech Stack

* **Python**
* **FastAPI**
* **Streamlit**
* **Scikit-learn**
* **NumPy**
* **Matplotlib**
* **Pydantic**

---

# 🩺 AURA — Health Intelligence Module

AURA evaluates physical wellbeing using lifestyle metrics such as:

* Sleep hours
* Activity level
* Stress levels
* Diet quality
* Heart rate

### Features

* Health score prediction
* Wellness recommendations
* Lifestyle risk analysis
* Real-time API endpoint

### Endpoint

```bash
POST /predict_health
```

---

# 💰 FINESIGHT — Financial Intelligence Module

FINESIGHT analyzes personal finance stability and investment behavior.

### Inputs

* Income
* Expenses
* Savings
* Credit score
* Market sentiment
* Risk tolerance

### Outputs

* Financial health score
* Risk profile classification
* Investment allocation suggestions
* Financial advice engine

### Risk Profiles

* Conservative
* Moderate
* Aggressive

### Endpoint

```bash
POST /predict_finance
```

---

# 🧠 SYNAPSE — Behavioral Intelligence Module

SYNAPSE predicts focus, productivity, and behavioral stability using machine learning.

### ML Model

* Random Forest Regressor

### Behavioral Metrics

* Mood
* Sleep
* Focus hours
* Screen time
* Distractions
* Stress
* Caffeine intake

### Outputs

* Focus score
* Burnout detection
* Productivity insights
* Cognitive optimization suggestions

### Endpoint

```bash
POST /predict_behavior
```

---

# 💠 AXION — Decision & Ethical Intelligence

AXION is the reasoning core of GENESIS.

It evaluates:

* Logic
* Emotion
* Risk tolerance
* Ethical priority

to generate a:

## 🧭 Decision Rationality Index (DRI)

AXION helps determine whether a decision is:

* Rational
* Emotionally biased
* Ethically balanced
* High-risk

### Features

* Ethical analysis
* Rationality scoring
* Decision optimization
* Cross-module integration

---

# 🌌 GENESIS Fusion Engine

The Fusion Engine is the heart of the system.

It:

1. Collects outputs from all modules
2. Computes the **Life Intelligence Index (LII)**
3. Generates short-term, medium-term, and long-term recommendations
4. Visualizes system-wide performance

### LII Formula

```python
LII = (Health × 0.4) + (Finance × 0.3) + (Behavior × 0.3)
```

---

# 📊 Features

✅ Real-time multi-module intelligence
✅ AI-powered life recommendations
✅ Decision optimization system
✅ Financial planning engine
✅ Productivity prediction
✅ Ethical reasoning engine
✅ Visual analytics dashboard
✅ Modular microservice architecture
✅ FastAPI backend services
✅ Interactive Streamlit UI

---

# 🖥️ Project Structure

```bash
GENESIS/
│
├── aura_core/
│   ├── main.py
│   └── ui_dashboard.py
│
├── finesight_core/
│   ├── main.py
│   └── ui_dashboard.py
│
├── synapse_core/
│   ├── main.py
│   └── ui_dashboard.py
│
├── axion_core/
│   ├── axion.py
│   ├── main.py
│   └── ui_dashboard.py
│
├── genesis_fusion/
│   └── fusion_dashboard.py
│
├── README.md
├── start_genesis.bat
└── .gitignore
```

---

# ▶️ Running The Project

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Start Backend Services

### AURA

```bash
uvicorn aura_core.main:app --reload --port 8001
```

### FINESIGHT

```bash
uvicorn finesight_core.main:app --reload --port 8002
```

### SYNAPSE

```bash
uvicorn synapse_core.main:app --reload --port 8003
```

### AXION

```bash
uvicorn axion_core.main:app --reload --port 8004
```

---

## 3️⃣ Launch GENESIS Fusion Dashboard

```bash
streamlit run genesis_fusion/fusion_dashboard.py
```

---

# 🧪 Example Workflow

1. User inputs health, finance, and behavioral data
2. GENESIS queries all AI modules
3. Scores are fused into the Life Intelligence Index
4. AXION evaluates decision stability
5. The system generates:

   * Immediate actions
   * Long-term recommendations
   * Ethical insights
   * Financial strategies

---

# 🔮 Future Vision

Planned future upgrades:

* 🧬 Personalized AI memory
* 📈 Real-world financial APIs
* ⌚ Wearable integration
* 🤖 LLM-powered life coaching
* 🌍 Cloud deployment
* 📱 Mobile companion app
* 🛰️ Predictive life simulation engine

---

# 🛡️ Disclaimer

GENESIS is an experimental AI research project designed for educational and analytical purposes.

It does **not** replace:

* Medical professionals
* Financial advisors
* Mental health experts
* Legal consultants

Always use professional judgment for real-world decisions.

---

# 👨‍💻 Authors

Kaushik ,  Prabhanjan , Vishnu Govind and Aadhitya Keshav☕⚡

**GENESIS 5.0** — *Engineering intelligence for human decisions.*
