@echo off
title 🌐 GENESIS 5.0 - Multi-Module Launcher

echo ================================================
echo        🚀 Starting GENESIS 5.0
echo ================================================

REM ================================
REM AXION API
REM ================================
echo [1/5] Starting AXION API on port 8000...
start cmd /k "cd axion_core && python -m uvicorn main:app --reload --port 8000"

REM ================================
REM AURA API
REM ================================
echo [2/5] Starting AURA API on port 8001...
start cmd /k "cd aura_core && python -m uvicorn main:app --reload --port 8001"

REM ================================
REM FINESIGHT API
REM ================================
echo [3/5] Starting FINESIGHT API on port 8002...
start cmd /k "cd finesight_core && python -m uvicorn main:app --reload --port 8002"

REM ================================
REM SYNAPSE API
REM ================================
echo [4/5] Starting SYNAPSE API on port 8003...
start cmd /k "cd synapse_core && python -m uvicorn main:app --reload --port 8003"

REM Wait for APIs to initialize
timeout /t 5 >nul

REM ================================
REM GENESIS FUSION DASHBOARD
REM ================================
echo [5/5] Starting GENESIS Fusion Dashboard on port 8500...
start cmd /k "cd genesis_fusion && streamlit run fusion_dashboard.py --server.port 8500"

echo ================================================
echo ✅ GENESIS 5.0 fully launched
echo 🌍 Open: http://localhost:8500
echo ================================================

pause