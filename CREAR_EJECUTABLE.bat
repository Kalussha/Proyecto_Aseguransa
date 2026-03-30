@echo off
chcp 65001 > nul
echo ============================================
echo   Crear Ejecutable (.exe) STANDALONE
echo ============================================
echo.
echo Este script creará un archivo .exe completamente
echo INDEPENDIENTE que NO requiere instalar Python
echo ni ninguna otra dependencia
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado
    echo.
    echo Necesitas Python solo para crear el ejecutable
    echo Una vez creado, el .exe funcionará en cualquier PC
    echo sin necesidad de Python
    echo.
    pause
    exit /b 1
)

echo Instalando PyInstaller...
python -m pip install --upgrade pyinstaller

echo.
echo Creando ejecutable STANDALONE...
echo Esto puede tardar 5-10 minutos, por favor espera...
echo.

REM Limpiar builds anteriores
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist GestionPolizas.spec del GestionPolizas.spec

REM Crear el ejecutable con todas las dependencias incluidas
python -m PyInstaller --onefile --windowed --name=GestionPolizas --hidden-import=customtkinter --hidden-import=openpyxl --hidden-import=sqlite3 --hidden-import=PIL._tkinter_finder --collect-all customtkinter --noconfirm main.py

echo.
if not exist "dist\GestionPolizas.exe" (
    echo [ERROR] No se pudo crear el ejecutable
    echo Verifica que no haya errores en la salida anterior
    pause
    exit /b 1
)

echo Verificando archivo creado...
dir "dist\GestionPolizas.exe"

echo.
echo ============================================
echo   ✓ EJECUTABLE CREADO EXITOSAMENTE
echo ============================================
echo.
echo Ubicación: dist\GestionPolizas.exe
echo.
echo ✓ Es COMPLETAMENTE INDEPENDIENTE
echo ✓ NO requiere instalar Python
echo ✓ NO requiere instalar librerías
echo ✓ Funciona en cualquier PC con Windows 7 o superior
echo.
echo CÓMO DISTRIBUIR:
echo 1. Copia el archivo "dist\GestionPolizas.exe"
echo 2. Envíalo a cualquier PC con Windows
echo 3. Ejecútalo con doble clic
echo 4. La base de datos se creará automáticamente
echo.
echo NOTA: El ejecutable pesa entre 50-100 MB porque incluye
echo Python y todas las librerías necesarias.
echo.
echo PARA PROBAR:
echo 1. Ve a: dist\
echo 2. Doble clic en: GestionPolizas.exe
echo.
pause
