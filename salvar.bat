@echo off
title INN - Salvar e Publicar
chcp 65001 > nul
cd /d "C:\_a\inn"

:: ── Versão atual ──────────────────────────────
set /p VER=<version.txt
echo.
echo ═══════════════════════════════════════════
echo  INN v%VER%  -  Salvar e Publicar
echo ═══════════════════════════════════════════

:: ── Backup automático com timestamp ───────────
for /f "tokens=1-3 delims=/" %%a in ("%date%") do set DT=%%c%%b%%a
for /f "tokens=1-2 delims=:" %%a in ("%time: =0%") do set HR=%%a%%b
set BACKUP=backups\index_%DT%_%HR%.html
copy "index.html" "%BACKUP%" > nul
echo [BACKUP] Salvo em: %BACKUP%

:: ── Confirma mensagem de commit ───────────────
echo.
set /p MSG=Descricao da mudanca (ou ENTER para padrao):
if "%MSG%"=="" set MSG=Atualizacao automatica

:: ── Bump de versao ────────────────────────────
set /p VER_NUM=<version.txt
set /a VER_NOVA=%VER_NUM: =%+1
echo 1.0%VER_NOVA%> version.txt
echo {"version":"1.0%VER_NOVA%"}> version.json

:: ── Git commit e push ─────────────────────────
echo.
echo [1/2] Commitando...
git add index.html version.txt version.json
git commit -m "INN v1.0%VER_NOVA% - %MSG%"

echo.
echo [2/2] Publicando no Vercel via GitHub...
git push origin main

if %errorlevel% equ 0 (
  echo.
  echo ═══════════════════════════════════════════
  echo  Publicado com sucesso!
  echo  Versao: v1.0%VER_NOVA%
  echo  URL: https://inn-sepia.vercel.app
  echo ═══════════════════════════════════════════
  echo.
  set /p ABRIR=Abrir no navegador? (S/N):
  if /i "%ABRIR%"=="S" start https://inn-sepia.vercel.app
) else (
  echo [ERRO] Falha no push. Verifique a conexao.
)

echo.
pause
