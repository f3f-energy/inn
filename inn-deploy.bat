@echo off
title INN Deploy
chcp 65001 > nul
cd /d "C:\_a\inn"

set LINK_VERCEL=https://inn-sepia.vercel.app

cls
echo.
echo ═══════════════════════════════════════════
echo  INN - Deploy Rapido
echo ═══════════════════════════════════════════
echo.

echo [1/2] Sincronizando com GitHub...
git pull origin main
if %errorlevel% neq 0 ( echo [ERRO] Falha ao sincronizar. & pause & exit /b 1 )

echo.
echo [2/2] Publicando...
git push origin main

if %errorlevel% equ 0 (
  echo.
  echo ═══════════════════════════════════════════
  echo  Deploy concluido!
  echo  %LINK_VERCEL%
  echo ═══════════════════════════════════════════
  echo.
  set /p ABRIR=Abrir no navegador? (S/N):
  if /i "%ABRIR%"=="S" start %LINK_VERCEL%
) else (
  echo [ERRO] Falha no push.
)

echo.
pause
