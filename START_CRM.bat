@echo off
color 0A
title Django CRM System

cls
echo.
echo.
echo          ╔══════════════════════════════════════════════╗
echo          ║                                              ║
echo          ║         Django CRM System v1.0               ║
echo          ║         Customer Relationship Manager        ║
echo          ║                                              ║
echo          ╚══════════════════════════════════════════════╝
echo.
echo.

REM Change to script directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist venv\ (
    echo [X] ERROR: Virtual environment not found!
    echo.
    echo Please run INSTALL.bat first to set up the application.
    echo.
    pause
    exit /b 1
)

echo     [√] Activating virtual environment...
call venv\Scripts\activate

echo     [√] Checking database...
if not exist db.sqlite3 (
    echo     [!] Database not found, creating...
    python manage.py migrate --noinput
)

echo     [√] Starting Django server...
echo.
echo     ┌──────────────────────────────────────────────────┐
echo     │                                                  │
echo     │   CRM System is now RUNNING!                     │
echo     │                                                  │
echo     │   Opening browser automatically...               │
echo     │                                                  │
echo     │   ► Access URL: http://127.0.0.1:8000           │
echo     │   ► Admin Panel: http://127.0.0.1:8000/admin    │
echo     │                                                  │
echo     │   To STOP the server:                           │
echo     │   • Close this window, OR                       │
echo     │   • Press Ctrl+C                                │
echo     │                                                  │
echo     └──────────────────────────────────────────────────┘
echo.

REM Wait 2 seconds then open browser
timeout /t 2 /nobreak >nul
start http://127.0.0.1:8000

REM Start Django server
python manage.py runserver

REM This line runs when server stops
echo.
echo Server stopped.
pause