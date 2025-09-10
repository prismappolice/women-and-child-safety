@echo off
cd /d "d:\new ap women safety"
echo Adding files to git...
git add .
echo Committing changes...
git commit -m "Fixed volunteer status checking database connection issue - removed duplicate code after finally block"
echo Getting commit hash...
git rev-parse HEAD
echo.
echo Commit completed successfully!
pause
