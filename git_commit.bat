@echo off
cd /d "d:\new ap women safety"
echo Current directory:
cd
echo.
echo Git status:
git status
echo.
echo Adding all files:
git add .
echo.
echo Committing changes:
git commit -m "Updated district data and fixed admin connection issues - main website now reflects database changes"
echo.
echo Git log (last 3 commits):
git log --oneline -3
pause
