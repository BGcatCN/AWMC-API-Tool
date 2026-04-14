::This program uses GB2312(ANSI) encoding.
::此程序采用GB2312(ANSI)编码。
@echo off
::我操了我真受不了这个傻逼ansi了
::我草我真服了
::不用ansi还打不开，行吧，我屈服了哈哈。。。
::娘希匹




:menu
color 07
echo 欢迎使用AWMC工具箱!
echo 1. 上传B50
echo 2. 检测API状态
echo 3. 退出
set /p choice="选择 (1-3): "
if "%choice%"=="1" goto upload_b50
if "%choice%"=="2" goto mai_ping
if "%choice%"=="3" goto end
echo 无效选择...
goto menu

::B50上传选择页
::话说编码为什么会爆了，我也没动啊

:upload_b50
color 07
echo 请选择需要上传的查分器:
echo 1.上传水鱼（upload_b50_fish.py）
echo 2.上传落雪（upload_b50_lx.py）
echo 3.返回菜单
set /p choice="选择(1-3):"
if "%choice%"=="1" goto upload_b50_fish
if "%choice%"=="2" goto upload_b50_lx
if "%choice%"=="3" goto menu
echo 无效选择...
goto upload_b50

:upload_b50_fish
python upload_b50_fish.py
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
color 07
echo.
choice /c YN /n /m "脚本执行已结束，要返回菜单吗? (Y/N): " >nul
if errorlevel 2 goto end
if errorlevel 1 goto menu
goto end

:end
