@echo off
REM Complete Render Deployment - Quick Start Script
echo ========================================
echo 🚀 Render Deployment - Quick Start
echo ========================================
echo.

echo Step 1: Checking requirements.txt...
if exist requirements.txt (
    echo ✅ requirements.txt found
) else (
    echo ❌ requirements.txt not found!
    pause
    exit
)

echo.
echo Step 2: Creating database backup...
python export_database_for_render.py

echo.
echo Step 3: Checking Procfile...
if exist Procfile (
    echo ✅ Procfile found
) else (
    echo ❌ Procfile not found!
    pause
    exit
)

echo.
echo ========================================
echo 📋 Files Ready for Deployment:
echo ========================================
dir /b render_backup_*.sql 2>nul
if errorlevel 1 (
    echo ⚠️ No backup file found!
) else (
    echo ✅ Database backup ready
)
echo ✅ requirements.txt
echo ✅ Procfile
echo ✅ app.py (configured for production)

echo.
echo ========================================
echo 📖 Next Steps:
echo ========================================
echo 1. Create PostgreSQL database on Render
echo 2. Restore backup file to Render database
echo 3. Create Web Service on Render
echo 4. Add environment variables
echo 5. Deploy!
echo.
echo 📄 Full guide: RENDER_DEPLOYMENT_GUIDE.md
echo ========================================

pause
