@echo off
chcp 65001 > nul
echo ============================================
echo   Sistema de Gestión de Pólizas de Seguros
echo ============================================
echo.
echo Instalando dependencias...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH
    echo.
    echo Por favor, instala Python desde: https://www.python.org/downloads/
    echo Asegúrate de marcar "Add Python to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

echo Python detectado correctamente
echo.

REM Actualizar pip
echo Actualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando paquetes necesarios...
pip install -r requirements.txt

echo.
echo ============================================
echo   ✓ Instalación completada exitosamente
echo ============================================
echo.
echo Ahora puedes ejecutar la aplicación con EJECUTAR.bat
echo.
pause
