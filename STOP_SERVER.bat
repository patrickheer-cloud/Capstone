@echo off
color 0C
title Django CRM - Stop Server

echo.
echo Stopping Django CRM server...
echo.

REM Find and kill Python processes running on port 8000
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo [√] Server stopped successfully
echo.
timeout /t 2 /nobreak >nul