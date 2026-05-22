@echo off
title 🌐 GENESIS 5.0 - Multi-Module Launcher
echo ================================================
echo     🚀 Starting GENESIS 5.0 AI Ecosystem
echo ================================================

REM ---- AXION BACKEND ----
echo [1/5] Starting AXION backend on port 8000...
start cmd /k "cd axion_core && python -m uvicorn main:app --reload --port 8000"

REM ---- AURA ----
echo [2/5] Starting AURA on port 8001...
start cmd /k "cd aura_core && streamlit run ui_dashboard.py --server.port 8001"

REM ---- FINESIGHT ----
echo [3/5] Starting FINESIGHT on port 8002...
start cmd /k "cd finesight_core && streamlit run ui_dashboard.py --server.port 8002"

REM ---- SYNAPSE ----
echo [4/5] Starting SYNAPSE on port 8003...
start cmd /k "cd synapse_core && streamlit run ui_dashboard.py --server.port 8003"

REM ---- FUSION DASHBOARD ----
echo [5/5] Starting GENESIS FUSION on port 8500...
start cmd /k "cd genesis_fusion && streamlit run fusion_dashboard.py --server.port 8500"

echo -----------------------------------------------
echo ✅ All modules launched. Open http://localhost:8500
echo -----------------------------------------------
pause
