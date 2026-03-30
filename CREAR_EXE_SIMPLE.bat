@echo off
chcp 65001 > nul
title Crear Ejecutable - Sistema de Pólizas
color 0A

echo.
echo ╔════════════════════════════════════════════════════════╗
echo ║  CREAR EJECUTABLE STANDALONE (.EXE)                    ║
echo ║  Sistema de Gestión de Pólizas de Seguros             ║
echo ╚════════════════════════════════════════════════════════╝
echo.

echo [1/5] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo.
    echo ✗ ERROR: Python no está instalado
    echo.
    echo Necesitas instalar Python primero desde:
    echo https://www.python.org/downloads/
    echo.
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)
python --version
echo ✓ Python encontrado

echo.
echo [2/5] Instalando/Actualizando PyInstaller...
python -m pip install --upgrade pyinstaller
if errorlevel 1 (
    color 0C
    echo.
    echo ✗ ERROR: No se pudo instalar PyInstaller
    pause
    exit /b 1
)
echo ✓ PyInstaller instalado

echo.
echo [3/5] Limpiando archivos anteriores...
if exist build (
    rmdir /s /q build
    echo ✓ Carpeta 'build' eliminada
)
if exist dist (
    rmdir /s /q dist
    echo ✓ Carpeta 'dist' eliminada
)
if exist *.spec (
    del /q *.spec
    echo ✓ Archivos .spec eliminados
)

echo.
echo [4/5] Creando ejecutable...
echo Este proceso puede tardar 5-10 minutos, por favor espera...
echo.

python -m PyInstaller --onefile --windowed --name=GestionPolizas --hidden-import=customtkinter --hidden-import=openpyxl --hidden-import=sqlite3 --hidden-import=PIL._tkinter_finder --collect-all customtkinter --noconfirm main.py

echo.
echo [5/5] Verificando resultado...

if exist "dist\GestionPolizas.exe" (
    color 0A
    echo.
    echo ╔════════════════════════════════════════════════════════╗
    echo ║  ✓✓✓ EJECUTABLE CREADO EXITOSAMENTE ✓✓✓              ║
    echo ╚════════════════════════════════════════════════════════╝
    echo.
    echo Ubicación: %CD%\dist\GestionPolizas.exe
    
    REM Obtener tamaño del archivo
    for %%A in ("dist\GestionPolizas.exe") do (
        set size=%%~zA
    )
    echo Tamaño: aproximadamente %size% bytes
    
    echo.
    echo CARACTERÍSTICAS:
    echo ✓ Completamente independiente
    echo ✓ NO requiere instalar Python
    echo ✓ NO requiere instalar librerías
    echo ✓ Funciona en Windows 7, 8, 10, 11
    echo ✓ Portable - copia y ejecuta
    echo.
    echo CÓMO USAR:
    echo 1. Ve a la carpeta "dist"
    echo 2. Copia "GestionPolizas.exe" donde quieras
    echo 3. Doble clic para ejecutar
    echo 4. ¡Listo!
    echo.
    echo ¿Quieres probar el ejecutable ahora? (S/N)
    set /p respuesta=
    if /i "%respuesta%"=="S" (
        echo.
        echo Ejecutando...
        start "" "dist\GestionPolizas.exe"
    )
) else (
    color 0C
    echo.
    echo ╔════════════════════════════════════════════════════════╗
    echo ║  ✗✗✗ ERROR: NO SE PUDO CREAR EL EJECUTABLE ✗✗✗      ║
    echo ╚════════════════════════════════════════════════════════╝
    echo.
    echo Posibles causas:
    echo - Errores en el código Python
    echo - Falta de permisos
    echo - Antivirus bloqueando PyInstaller
    echo - Espacio insuficiente en disco
    echo.
    echo Revisa los mensajes de error arriba
    echo.
    pause
    exit /b 1
)

echo.
pause
