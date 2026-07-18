@echo off
title INN Developer Console v2.0
color 0B
mode con: cols=90 lines=35

:MENU
cls

echo.
echo ================================================================================
echo.
echo                          INN DEVELOPER CONSOLE
echo.
echo                         Inn Technology
echo.
echo ================================================================================
echo.
echo Projeto............... INN CRM
echo Versao................ 2.0 Foundation
echo Branch................ desenvolvimento
echo Ambiente.............. Desenvolvimento
echo.
echo ================================================================================
echo.
echo [ 1 ] Abrir VS Code
echo [ 2 ] Git Status
echo [ 3 ] Git Pull
echo [ 4 ] Git Commit
echo [ 5 ] Git Push
echo [ 6 ] Abrir INN
echo [ 7 ] GitHub
echo [ 8 ] Supabase
echo [ 9 ] Backup do Projeto
echo [10 ] Abrir Pasta
echo [11 ] CMD
echo [12 ] PowerShell
echo [13 ] Vercel
echo [14 ] Criar Documentacao
echo [15 ] Sair
echo.
echo ================================================================================
set /p op=Escolha:

if "%op%"=="1" (
    code .
    goto MENU
)

if "%op%"=="2" (
    git status
    pause
    goto MENU
)

if "%op%"=="3" (
    git pull
    pause
    goto MENU
)

if "%op%"=="4" (
    set /p msg=Mensagem:
    git add .
    git commit -m "%msg%"
    pause
    goto MENU
)

if "%op%"=="5" (
    git push origin desenvolvimento
    pause
    goto MENU
)

if "%op%"=="6" (
    start index.html
    goto MENU
)

if "%op%"=="7" (
    start https://github.com/f3f-energy/inn
    goto MENU
)

if "%op%"=="8" (
    start https://supabase.com/dashboard/project/nmzifhqivuhdfwlelmxp
    goto MENU
)

if "%op%"=="9" (
    if not exist backups mkdir backups

    set data=%date:~6,4%-%date:~3,2%-%date:~0,2%

    xcopy . backups\backup_%data%\ /E /I /Y >nul

    echo.
    echo Backup concluido.
    pause
    goto MENU
)

if "%op%"=="10" (
    explorer .
    goto MENU
)

if "%op%"=="11" (
    start cmd /k "cd /d %cd%"
    goto MENU
)

if "%op%"=="12" (
    start powershell
    goto MENU
)

if "%op%"=="13" (
    start https://vercel.com/dashboard
    goto MENU
)

if "%op%"=="14" (
    if not exist docs mkdir docs
    echo Documentacao pronta.
    pause
    goto MENU
)

if "%op%"=="15" (
    exit
)

goto MENU