@echo off
:menu
color 07
echo ѡ����Ҫ���еĽű�����:
echo 1. �ϴ�B50
echo 2. ���API״̬
echo 3. �˳�
set /p choice="ѡ�� (1-3): "
if "%choice%"=="1" goto upload_b50
if "%choice%"=="2" goto mai_ping
if "%choice%"=="3" goto end
echo ��Чѡ��...
goto menu

::�˵�
::����ľ�ֻ��һ���˵�...

:upload_b50
color 07
echo ѡ����Ҫ���еĽű�:
echo 1.�ϴ�ˮ�㣨upload_b50.py��
echo 2.�ϴ���ѩ��upload_b50_lx.py��
echo 3.����
set /p choice="ѡ��(1-3):"
if "%choice%"=="1" goto upload_b50_fish
if "%choice%"=="2" goto upload_b50_lx
if "%choice%"=="3" goto menu
echo ��Чѡ��...
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
choice /c YN /n /m "�ű������ѽ������ص��˵���? (Y/N): " >nul
if errorlevel 2 goto end
if errorlevel 1 goto menu
goto end

:end
