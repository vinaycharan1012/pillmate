@echo off
echo =======================================================================
echo   Starting MediMate (ARISE) Health Prototype Web Server...
echo   Opening http://localhost:8080 in your browser...
echo =======================================================================
cd /d "%~dp0health-prototype"
python server.py
pause
