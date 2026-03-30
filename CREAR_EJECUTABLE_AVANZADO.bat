@echo off
chcp 65001 > nul
echo ============================================
echo   Crear Ejecutable PORTABLE (Recomendado)
echo ============================================
echo.
echo Esta versión crea una CARPETA portable que:
echo - Inicia más rápido que el .exe único
echo - Es más fácil de actualizar
echo - Incluye TODO lo necesario
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado
    echo.
    pause
    exit /b 1
)

echo Instalando PyInstaller...
python -m pip install --upgrade pyinstaller

echo.
echo Creando versión PORTABLE...
echo Esto puede tardar 5-10 minutos, por favor espera...
echo.

REM Limpiar builds anteriores
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist GestionPolizasPortable.spec del GestionPolizasPortable.spec

REM Crear versión portable (carpeta con ejecutable)
python -m PyInstaller --onedir --windowed --name=GestionPolizasPortable --hidden-import=customtkinter --hidden-import=openpyxl --hidden-import=sqlite3 --hidden-import=PIL._tkinter_finder --collect-all customtkinter --noconfirm main.py

echo.
if not exist "dist\GestionPolizasPortable" (
    echo [ERROR] No se pudo crear el ejecutable
    echo Verifica que no haya errores en la salida anterior
    pause
    exit /b 1
)

echo Verificando archivos creados...
dir "dist\GestionPolizasPortable"

echo.
echo Creando archivos adicionales...

REM Crear archivo de inicio
echo @echo off> "dist\GestionPolizasPortable\INICIAR_APLICACION.bat"
echo start GestionPolizasPortable.exe>> "dist\GestionPolizasPortable\INICIAR_APLICACION.bat"

REM Crear README
(
echo SISTEMA DE GESTION DE POLIZAS DE SEGUROS
echo ==========================================
echo.
echo INSTRUCCIONES:
echo.
echo 1. Doble clic en "INICIAR_APLICACION.bat"
echo    O doble clic en "GestionPolizasPortable.exe"
echo.
echo 2. La base de datos se creara automaticamente
echo.
echo CARACTERISTICAS:
echo - No requiere instalacion
echo - No requiere Python
echo - Portable: Copia la carpeta a un USB
echo - Compatible: Windows 7, 8, 10, 11
) > "dist\GestionPolizasPortable\LEEME.txt"

echo.
echo ============================================
echo   ✓ VERSION PORTABLE CREADA EXITOSAMENTE
echo ============================================
echo.
echo Ubicación: dist\GestionPolizasPortable\
echo Ejecutable: GestionPolizasPortable.exe
echo.
echo VENTAJAS de esta versión:
echo ✓ Inicia más rápido
echo ✓ Ocupa menos espacio en RAM
echo ✓ Más fácil de actualizar
echo ✓ Puedes copiar la carpeta completa a un USB
echo.
echo PARA DISTRIBUIR:
echo 1. Ve a la carpeta "dist"
echo 2. Comprime la carpeta "GestionPolizasPortable" en ZIP
echo 3. Envía el archivo ZIP
echo 4. El usuario descomprime y ejecuta
echo.
echo PARA PROBAR:
echo 1. Ve a: dist\GestionPolizasPortable
echo 2. Doble clic en: GestionPolizasPortable.exe
echo.
pause
