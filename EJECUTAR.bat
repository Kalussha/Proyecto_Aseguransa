@echo off
chcp 65001 > nul
echo ============================================
echo   Sistema de Gestión de Pólizas de Seguros
echo ============================================
echo.
echo Iniciando aplicación...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado
    echo.
    echo Ejecuta primero INSTALAR.bat
    echo.
    pause
    exit /b 1
)

REM Ejecutar la aplicación
python main.py

REM Si hay un error, pausar para ver el mensaje
if errorlevel 1 (
    echo.
    echo [ERROR] Ocurrió un error al ejecutar la aplicación
    echo.
    pause
)
