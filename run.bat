@echo off
python --version >nul 2>&1
if errorlevel 1 (
    echo Python 未安装或不在 PATH 中。
    echo 请安装 Python 并将其添加到 PATH。
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
python api_request.py
pause