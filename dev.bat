@echo off
title INN Developer
color 0A
setlocal EnableDelayedExpansion

:: ===========================================================
:: CONFIGURACAO
:: ===========================================================

set ROOT=%~dp0
cd /d "%ROOT%"

:: ===========================================================
:: MENU
:: ===========================================================

:MENU
cls

echo.
echo ================================================================
echo                           INN DEVELOPER
echo ================================================================
echo.

echo Projeto : %CD%

for /f %%i in ('git branch --show-current 2^>nul') do set BRANCH=%%i
if not defined BRANCH set BRANCH=Nao encontrado

echo Branch  : !BRANCH!

git status --porcelain > "%TEMP%\git.tmp"

for %%A in ("%TEMP%\git.tmp") do set SIZE=%%~zA

if "!SIZE!"=="0" (
    echo Git     : LIMPO
) else (
    echo Git     : ALTERACOES
)

del "%TEMP%\git.tmp" >nul 2>nul

echo.
echo ================================================================
echo.
echo  1 - Abrir VS Code
echo  2 - Git Status
echo  3 - Git Pull
echo  4 - Git Commit
echo  5 - Git Push
echo  6 - Backup
echo  7 - Abrir Explorer
echo  8 - Abrir GitHub
echo  9 - Abrir Supabase
echo 10 - Abrir Vercel
echo 11 - Executar INN
echo 12 - Sair
echo.
echo ================================================================
echo.

set /p OP=Opcao:

if "%OP%"=="1" goto VSCODE
if "%OP%"=="2" goto STATUS
if "%OP%"=="3" goto PULL
if "%OP%"=="4" goto COMMIT
if "%OP%"=="5" goto PUSH
if "%OP%"=="6" goto BACKUP
if "%OP%"=="7" goto EXPLORER
if "%OP%"=="8" goto GITHUB
if "%OP%"=="9" goto SUPABASE
if "%OP%"=="10" goto VERCEL
if "%OP%"=="11" goto RUN
if "%OP%"=="12" exit

goto MENU

:: ===========================================================

:VSCODE
code .
goto MENU

:: ===========================================================

:STATUS
cls
git status
echo.
pause
goto MENU

:: ===========================================================

:PULL
cls
git pull
echo.
pause
goto MENU

:: ===========================================================

:COMMIT
cls
echo.
set /p MSG=Mensagem do commit:

git add .

git commit -m "%MSG%"

echo.
pause
goto MENU

:: ===========================================================

:PUSH
cls
git push origin desenvolvimento
echo.
pause
goto MENU

:: ===========================================================

:BACKUP

if not exist backups mkdir backups

for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set DATA=%%i

echo.
echo Criando Backup...

powershell -NoProfile -Command ^
"Compress-Archive -Path '%ROOT%*' -DestinationPath '%ROOT%backups\backup_%DATA%.zip' -Force"

echo.
echo Backup concluido.
echo.
pause
goto MENU

:: ===========================================================

:EXPLORER
start explorer .
goto MENU

:: ===========================================================

:GITHUB
start https://github.com/f3f-energy/inn
goto MENU

:: ===========================================================

:SUPABASE
start https://supabase.com/dashboard/project/nmzifhqivuhdfwlelmxp
goto MENU

:: ===========================================================

:VERCEL
start https://vercel.com/dashboard
goto MENU

:: ===========================================================

:RUN

if exist index.html (
    start index.html
) else (
    echo index.html nao encontrado.
    pause
)

goto MENU