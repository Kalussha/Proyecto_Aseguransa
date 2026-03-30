# 🚗 Sistema de Gestión de Pólizas de Seguros de Vehículos

Aplicación de escritorio moderna para Windows desarrollada con Python, CustomTkinter y SQLite.

## 📋 Características

- ✅ **Interfaz moderna y profesional** con CustomTkinter
- ✅ **Base de datos SQLite** local (sin necesidad de servidor)
- ✅ **Búsqueda universal en tiempo real** - Busca en TODOS los campos (nombre, domicilio, RFC, póliza, vehículo, etc.)
- ✅ **Gestión completa** de pólizas (Alta, Edición, Eliminación)
- ✅ **Alertas visuales** para vencimientos próximos (menos de 15 días)
- ✅ **Exportación a Excel** de pólizas individuales
- ✅ **Validación de RFC** (12-13 caracteres)
- ✅ **Sin licencias comerciales** - 100% código libre

## 🖥️ Requisitos del Sistema

- Windows 7 o superior
- Python 3.8 o superior

## 📦 Instalación y Uso

### 🎯 OPCIÓN 1: EJECUTABLE STANDALONE (SIN INSTALAR NADA)

**Si recibes solo el archivo .exe o carpeta portable:**

1. **Archivo único (.exe)**:
   - Doble clic en `GestionPolizas.exe`
   - ¡Listo! No requiere instalación

2. **Versión portable (carpeta)**:
   - Descomprime la carpeta ZIP
   - Doble clic en `INICIAR_APLICACION.bat` o el archivo `.exe`
   - ¡Funciona sin instalar nada!

✅ **NO requiere instalar Python**  
✅ **NO requiere instalar librerías**  
✅ **Funciona en cualquier Windows 7, 8, 10, 11**

---

### 💻 OPCIÓN 2: CREAR TU PROPIO EJECUTABLE

**Si tienes el código fuente y quieres crear el .exe:**

1. **Ejecutar** `INSTALAR.bat` (instala dependencias)

2. **Ejecutar** `INSTALAR_PYINSTALLER.bat` ⭐ **NUEVO - IMPORTANTE**
   - Instala PyInstaller correctamente
   - Evita el error "pyinstaller no se reconoce"

3. **Elegir UNA de estas opciones**:
   - 🟢 `CREAR_EXE_SIMPLE.bat` → **RECOMENDADO** - Simple y robusto
   - 🔵 `CREAR_EJECUTABLE.bat` → Archivo único (~100MB)  
   - 🟣 `CREAR_EJECUTABLE_AVANZADO.bat` → Versión portable (carpeta)

4. **Ejecutar como Administrador** (clic derecho → Ejecutar como admin)

5. Esperar 5-10 minutos

6. El ejecutable estará en la carpeta `dist`

7. Distribuir el .exe o carpeta portable

⚠️ **¿Error "pyinstaller no se reconoce"?** Ejecuta `INSTALAR_PYINSTALLER.bat` primero

⚠️ **¿Otros problemas?** Lee `SOLUCION_PROBLEMAS_EXE.txt`

📖 **Guía detallada:** `GUIA_CREAR_EJECUTABLE.txt`

---

### 🔧 OPCIÓN 3: Ejecutar desde Código Fuente

**Para desarrolladores:**

1. **Instalar Python** (si no lo tienes):
   - Descarga Python desde: https://www.python.org/downloads/
   - Durante la instalación, marca "Add Python to PATH"

2. **Doble clic en** `INSTALAR.bat`
   - Instala todas las dependencias

3. **Doble clic en** `EJECUTAR.bat`
   - Inicia la aplicación

**Manual:**
```bash
pip install -r requirements.txt
python main.py
```

## 📊 Estructura de Datos

### Bloque 1: Información Personal
- Nombre completo (obligatorio)
- Domicilio completo (Calle, No, CP, Colonia, Municipio, Estado)
- RFC (12-13 caracteres)
- Email

### Bloque 2: Datos de Póliza y Vehículo
- Compañía aseguradora
- Número de Póliza
- Endoso
- Inciso
- Vigencia (Inicio y Fin)
- Forma de pago (Mensual, Bimestral, Trimestral, Semestral, Anual, Contado)
- Fecha de vencimiento de pago
- Datos del vehículo (Marca, Modelo, Tipo/Versión, Año, Serie/VIN, Motor, Placas)
- Prima Total

## 🎯 Uso de la Aplicación

### Crear Nueva Póliza
1. Clic en el botón verde **"+ Nueva Póliza"**
2. Llenar los campos del formulario
3. Clic en **"💾 Guardar"**

### Buscar Pólizas
- Escribe en la barra de búsqueda superior
- La búsqueda es en tiempo real y busca en **TODOS los campos**:
  - **Datos Personales**: Nombre, Domicilio (Calle, Número, CP, Colonia, Municipio, Estado), RFC, Email
  - **Datos de Póliza**: Compañía, Número de Póliza, Endoso, Inciso
  - **Datos del Vehículo**: Marca, Modelo, Tipo/Versión, Año, Serie/VIN, Motor, Placas
- Ejemplo: Puedes buscar por "Toyota", "México", "HDI", un código postal, etc.

### Editar Póliza
1. Clic en una póliza de la lista lateral
2. Modificar los campos necesarios
3. Clic en **"💾 Guardar"**

### Eliminar Póliza
1. Seleccionar una póliza de la lista
2. Clic en **"🗑️ Eliminar"**
3. Confirmar la eliminación

### Exportar a Excel
1. Seleccionar una póliza de la lista
2. Clic en **"📊 Exportar a Excel"**
3. Elegir ubicación y nombre del archivo
4. El archivo Excel se guardará con todos los datos de la póliza

## ⚠️ Alertas de Vencimiento

Las pólizas se resaltan en **color rojo** cuando:
- La fecha de vencimiento de pago está a menos de 15 días
- La vigencia de la póliza expira en menos de 15 días

## 📁 Archivos del Proyecto

```
Asegurnasa/
├── main.py                        # Archivo principal de la aplicación
├── database.py                    # Gestor de base de datos SQLite
├── requirements.txt               # Dependencias de Python
├── INSTALAR.bat                   # Script instalación de dependencias
├── INSTALAR_PYINSTALLER.bat       # ⭐ Instalar PyInstaller (NUEVO)
├── EJECUTAR.bat                   # Script para ejecutar aplicación
├── CREAR_EXE_SIMPLE.bat           # 🟢 Crear .exe (RECOMENDADO)
├── CREAR_EJECUTABLE.bat           # 🔵 Crear .exe único (50-100 MB)
├── CREAR_EJECUTABLE_AVANZADO.bat  # 🟣 Crear versión portable
├── GUIA_CREAR_EJECUTABLE.txt      # Guía completa para crear .exe
├── SOLUCION_PROBLEMAS_EXE.txt     # ⚠️ Soluciones a problemas comunes
├── COMO_CREAR_EXE.txt             # Guía rápida
├── INSTRUCCIONES_USUARIO.txt      # Manual usuario final
├── LEEME_PRIMERO.txt              # Inicio rápido
├── README.md                      # Este archivo
└── seguros.db                     # Base de datos (se crea automáticamente)
```

### 📂 Carpeta dist/ (después de crear ejecutable)
```
dist/
├── GestionPolizas.exe                    # Ejecutable único standalone
└── GestionPolizas_Portable/              # Versión portable
    ├── GestionPolizasPortable.exe
    ├── INICIAR_APLICACION.bat
    ├── LEEME.txt
    └── [archivos de soporte]
```

## 🔧 Solución de Problemas

### Error: "Python no se reconoce como comando"
- Reinstala Python y asegúrate de marcar "Add Python to PATH" durante la instalación

### Error al importar customtkinter
- Ejecuta: `pip install --upgrade customtkinter`

### La base de datos no se crea
- Verifica que tengas permisos de escritura en la carpeta del proyecto

## 👨‍💻 Soporte Técnico

Para reportar problemas o sugerencias, contacta al desarrollador.

## 📄 Licencia

Este software es de código libre y puede ser usado sin restricciones comerciales.

---

**Desarrollado con ❤️ para Asegurnasa**
