@echo off
TITLE 3DGS PLY Standardizer

:: 1. 尝试直接运行 python
python --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python found! Running script...
    python ply_standardizer.py
    pause
    EXIT /B
)

:: 2. 如果失败，尝试 py (Windows Launcher)
py --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python Launcher found! Running script...
    py ply_standardizer.py
    pause
    EXIT /B
)

:: 3. 如果都找不到，报错并提示
echo ========================================================
echo [ERROR] Python is not found or not in your PATH.
echo ========================================================
echo.
echo To run this tool, you need to:
echo 1. Download Python from python.org
echo 2. During installation, CHECK "Add Python to PATH"
echo.
echo If you installed Python but see this error, you need to
echo add it to your System Environment Variables manually.
echo.
pause