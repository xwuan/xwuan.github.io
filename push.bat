@echo off
chcp 65001 >nul
echo =============================================
echo   Xwuan - Push code lên GitHub
echo   URL: https://github.com/xwuan/xwuan.github.io
echo =============================================
if exist "C:\Users\ADMIN\AppData\Local\Programs\Git\bin\bash.exe" (
    "C:\Users\ADMIN\AppData\Local\Programs\Git\bin\bash.exe" push.sh
) else (
    "C:\Program Files\Git\bin\bash.exe" push.sh
)
pause
