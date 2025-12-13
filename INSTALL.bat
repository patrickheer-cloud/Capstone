@echo off
color 0B
title Django CRM - Installation

echo.
echo     ╔════════════════════════════════════════════════╗
echo     ║        Django CRM System - Installer           ║
echo     ║                Version 1.0                     ║
echo     ╚════════════════════════════════════════════════╝
echo.
echo.

echo [Step 1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] ERROR: Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)
echo [√] Python found
python --version
echo.

echo [Step 2/5] Creating virtual environment...
if exist venv\ (
    echo [!] Virtual environment already exists, skipping...
) else (
    python -m venv venv
    echo [√] Virtual environment created
)
echo.

echo [Step 3/5] Activating virtual environment...
call venv\Scripts\activate