@echo off
chcp 65001 >nul
echo.
echo ========================================
echo   MD → HWPX 변환기 빌드 스크립트
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python이 설치되어 있지 않습니다.
    echo    https://www.python.org/downloads/ 에서 설치하세요.
    echo    설치 시 "Add Python to PATH" 체크를 꼭 하세요!
    pause
    exit /b 1
)

echo ⏳ 빌드 중... (1~2분 소요)
echo.
python "%~dp0build_exe.py"

echo.
pause
