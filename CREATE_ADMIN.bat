@echo off
color 0E
title Django CRM - Create Admin Account

echo.
echo ╔════════════════════════════════════════════════╗
echo ║      Create Administrator Account              ║
echo ╚════════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

if not exist venv\ (
    echo [X] ERROR: Please run INSTALL.bat first
    pause
    exit /b 1
)

call venv\Scripts\activate

echo This will create an admin account for the CRM system.
echo.
echo You'll be asked for:
echo   1. Username
echo   2. Email (optional - you can press Enter to skip)
echo   3. Password (typed characters won't be visible)
echo   4. Password confirmation
echo.
pause

python manage.py createsuperuser

echo.
echo ════════════════════════════════════════════════
echo Admin account created successfully!
echo You can now login at: http://127.0.0.1:8000/admin
echo ════════════════════════════════════════════════
echo.
pause