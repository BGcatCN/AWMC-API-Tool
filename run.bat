@echo off
:menu
echo 选择需要运行的脚本:
echo 1. 上传水鱼 (upload_b50.py)
echo 2. 上传落雪 (upload_b50_lx.py)
echo 3. 测试API状态 (mai_ping.py)
echo 4. 退出
set /p choice="选择 (1-4): "
if "%choice%"=="1" goto upload_b50
if "%choice%"=="2" goto upload_b50_lx
if "%choice%"=="3" goto mai_ping
if "%choice%"=="4" goto end
echo Invalid choice
pause
goto menu

:upload_b50
python upload_b50.py
call :after_run
goto end

:upload_b50_lx
python upload_b50_lx.py
call :after_run
goto end

:mai_ping
python mai_ping.py
call :after_run
goto end

:after_run
echo.
choice /c YN /n /m "脚本运行已结束，回到菜单吗? (Y = 回到菜单, N = 退出): " >nul
if errorlevel 2 goto end
if errorlevel 1 goto menu
goto end

:end
pause