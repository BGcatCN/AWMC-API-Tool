@echo off
echo 选择要运行的脚本：
echo 1. 上传水鱼 (upload_b50.py)
echo 2. 上传落雪 (upload_b50_lx.py)
set /p choice="请输入选择 (1 或 2): "
if "%choice%"=="1" goto upload_b50
if "%choice%"=="2" goto upload_b50_lx
echo 无效选择
goto end

:upload_b50
python upload_b50.py
goto end

:upload_b50_lx
python upload_b50_lx.py
goto end

:end
pause