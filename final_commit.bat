@echo off
cd /d "d:\new ap women safety"

echo === FINAL GIT COMMIT - ALL CHANGES ===
echo Current time: %date% %time%
echo.

echo Adding all files to git...
git add .

echo.
echo Committing all changes...
git commit -m "FINAL COMMIT: All AP Women Safety updates completed - 26 districts, admin fixes, data mapping, git tracking - %date%"

echo.
echo Checking status...
git status

echo.
echo Recent commits:
git log --oneline -3

echo.
echo === ALL CHANGES SAVED TO GIT ===
echo Your project is now fully backed up!
pause
