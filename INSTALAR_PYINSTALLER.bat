@echo off
chcp 65001 > nul
echo ============================================
echo   Instalar PyInstaller Correctamente
echo ============================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado
    echo.
    echo Instala Python desde: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python detectado:
python --version
echo.

echo Actualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando PyInstaller...
python -m pip install --upgrade pyinstaller

echo.
echo Verificando instalación...
python -m PyInstaller --version

if errorlevel 1 (
    echo.
    echo [ERROR] PyInstaller NO se instaló correctamente
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   ✓ PyInstaller instalado correctamente
echo ============================================
echo.
echo Ahora puedes ejecutar cualquiera de estos scripts:
echo - CREAR_EXE_SIMPLE.bat (RECOMENDADO)
echo - CREAR_EJECUTABLE.bat
echo - CREAR_EJECUTABLE_AVANZADO.bat
echo.
pause
