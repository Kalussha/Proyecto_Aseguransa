# 📘 GUÍA RÁPIDA - NUEVA INTERFAZ ASEGURNASA

## 🚀 INICIO RÁPIDO

### Ejecutar la Aplicación
```
1. Doble clic en main.py
   O ejecutar: python main.py
   
2. La ventana se abrirá centrada (1450x850 px)
```

---

## 🎯 FUNCIONES PRINCIPALES

### 1️⃣ BUSCAR PÓLIZAS
```
┌─────────────────────────────┐
│ 🔍 Panel Izquierdo          │
└─────────────────────────────┘

1. Escribe en el campo de búsqueda
2. La búsqueda es AUTOMÁTICA (en tiempo real)
3. Busca en TODOS los campos:
   ✅ Nombre del asegurado
   ✅ RFC, Email
   ✅ Número de póliza, Endoso, Inciso
   ✅ Compañía aseguradora
   ✅ Marca, Modelo, Placas, VIN
   ✅ Domicilio completo
   ✅ Y más...

4. El contador muestra: "📊 X pólizas encontradas"
```

**Ejemplo de búsqueda:**
- "Juan" → Busca en todos los campos
- "ABC123" → Encuentra póliza o placas
- "GNP" → Encuentra compañía aseguradora
- "Honda" → Encuentra marca del vehículo

---

### 2️⃣ CREAR NUEVA PÓLIZA
```
┌─────────────────────────────┐
│ ➕ Botón Verde              │
└─────────────────────────────┘

1. Clic en "➕ NUEVA PÓLIZA"
2. El formulario cambia a:
   "🆕 Nueva Póliza"
3. Completa los campos (solo Nombre es obligatorio)
4. Clic en "💾 GUARDAR PÓLIZA"
```

**Campos obligatorios:**
- ⭐ **Nombre Completo** (marcado con *)

**Validaciones automáticas:**
- RFC debe tener 12 o 13 caracteres
- Prima Total debe ser un número válido

---

### 3️⃣ EDITAR PÓLIZA EXISTENTE
```
┌─────────────────────────────┐
│ 📝 Seleccionar y Editar     │
└─────────────────────────────┘

1. Clic en cualquier póliza de la lista
2. El formulario se llena automáticamente
3. Título cambia a: "✏️ [Nombre del Asegurado]"
4. Modifica los campos necesarios
5. Clic en "💾 GUARDAR PÓLIZA"
```

---

### 4️⃣ ELIMINAR PÓLIZA
```
┌─────────────────────────────┐
│ 🗑️ Botón Rojo              │
└─────────────────────────────┘

1. Selecciona una póliza de la lista
2. Clic en "🗑️ ELIMINAR PÓLIZA"
3. Confirma la eliminación
   ⚠️ Esta acción NO se puede deshacer
```

---

### 5️⃣ EXPORTAR A EXCEL
```
┌─────────────────────────────┐
│ 📊 Exportar Individual      │
└─────────────────────────────┘

1. Selecciona una póliza
2. Clic en "📊 EXPORTAR A EXCEL"
3. Elige ubicación y nombre
4. Se crea archivo .xlsx con formato profesional
```

**Contenido del Excel:**
- Título: "PÓLIZA DE SEGURO DE VEHÍCULO"
- Información Personal completa
- Datos de Póliza detallados
- Información del Vehículo
- Formato profesional con negritas y organización

---

### 6️⃣ CANCELAR EDICIÓN
```
┌─────────────────────────────┐
│ ❌ Descartar Cambios        │
└─────────────────────────────┘

1. Durante cualquier edición
2. Clic en "❌ CANCELAR"
3. Vuelve al modo "Nueva Póliza"
4. Los cambios se descartan
```

---

## 🎨 ELEMENTOS VISUALES

### Colores de Estado

| Color | Significado | Uso |
|-------|-------------|-----|
| 🟢 Verde | Éxito/Guardar | Botón guardar, estado OK |
| 🔴 Rojo | Peligro/Alerta | Vencimientos < 15 días, eliminar |
| 🔵 Azul | Principal | Headers, secciones de póliza |
| 🟡 Amarillo | Advertencia | Sección de vehículo |
| 🔵 Cyan | Información | Sección personal |
| ⚪ Gris | Neutral | Cancelar, fondos |

### Iconos del Sistema

```
🏢 = Empresa/Sistema
📁 = Total de pólizas
📅 = Fecha
🔍 = Búsqueda
➕ = Nueva póliza
💾 = Guardar
❌ = Cancelar
📊 = Exportar
🗑️ = Eliminar
⚠️ = Alerta de vencimiento
✏️ = Editando
🆕 = Nueva
📄 = Detalles
👤 = Información Personal
📋 = Datos de Póliza
🚗 = Datos del Vehículo
⚙️ = Acciones
🟢 = Sistema operativo
```

---

## 📊 INFORMACIÓN DEL SISTEMA

### Header (Parte Superior)
```
╔════════════════════════════════════════════════╗
║ 🏢 ASEGURNASA                                  ║
║ Sistema de Gestión de Pólizas                  ║
║ 📅 [Fecha Actual] | 📁 [Total Pólizas]        ║
╚════════════════════════════════════════════════╝
```

### Footer (Parte Inferior)
```
╔════════════════════════════════════════════════╗
║ Sistema de Gestión de Pólizas v1.0            ║
║ 🟢 Sistema Operativo                           ║
╚════════════════════════════════════════════════╝
```

---

## ⚠️ ALERTAS VISUALES

### 🔴 Pólizas por Vencer
```
┌─────────────────────┐
│ ⚠️ Juan Pérez       │  ← Tarjeta ROJA
│ 📋 12345 • 🚗 ABC   │     con icono alerta
└─────────────────────┘

Condición:
- Vigencia Fin < 15 días
- Fecha Vencimiento Pago < 15 días
```

### ⚪ Pólizas Normales
```
┌─────────────────────┐
│ María González      │  ← Tarjeta GRIS
│ 📋 67890 • 🚗 XYZ   │     sin alerta
└─────────────────────┘
```

---

## 💡 CONSEJOS Y TRUCOS

### ✅ Búsqueda Eficiente
- Usa términos cortos y específicos
- No necesitas escribir todo: "Hon" encuentra "Honda"
- Busca por placas, póliza o nombre según necesites

### ✅ Navegación Rápida
- Usa Tab para moverte entre campos
- Enter en búsqueda actualiza inmediatamente
- Doble clic en póliza para editar más rápido

### ✅ Organización
- Las pólizas próximas a vencer aparecen en rojo
- Revisa regularmente el contador de pólizas
- Exporta periódicamente a Excel como respaldo

### ✅ Validación de Datos
- RFC: 12-13 caracteres automáticamente validado
- Fechas: Formato DD-MM-AAAA (ej: 31-12-2024)
- Prima: Solo acepta números (puede usar decimales)

### ✅ Campos de Fecha
Formato correcto:
- ✅ 2024-01-15
- ✅ 2024-12-31
- ❌ 15/01/2024 (incorrecto)
- ❌ 31-12-2024 (incorrecto)

---

## 📞 SOPORTE

### Base de Datos
- **Archivo:** seguros.db (creado automáticamente)
- **Ubicación:** Misma carpeta que main.py
- **Respaldo:** Copia seguros.db periódicamente

### Archivos Importantes
```
main.py              → Código principal
database.py          → Gestión de base de datos
seguros.db          → Base de datos SQLite
LEEME_PRIMERO.txt   → Instrucciones iniciales
README.md           → Documentación completa
```

### Crear Ejecutable
```
1. CREAR_EXE_SIMPLE.bat         (Recomendado)
2. CREAR_EJECUTABLE.bat         (Archivo único)
3. CREAR_EJECUTABLE_AVANZADO.bat (Carpeta portable)
```

---

## ✨ CARACTERÍSTICAS DESTACADAS

✅ **Búsqueda Universal** - Busca en más de 20 campos diferentes
✅ **Alertas Automáticas** - Detecta vencimientos próximos
✅ **Diseño Multi-columna** - Menos scroll, más eficiencia
✅ **Validación Inteligente** - RFC, números, campos requeridos
✅ **Export Profesional** - Excel con formato corporativo
✅ **Interface Intuitiva** - Iconos claros y colores significativos
✅ **Sin Instalación** - Base de datos local SQLite
✅ **Respaldo Fácil** - Copia simple del archivo .db

---

**Versión:** 1.0
**Última actualización:** Enero 2024
**Desarrollado por:** ASEGURNASA
