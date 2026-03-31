# 🔒 Validación de Campos Únicos - ASEGURANZA

## 📋 Campos Únicos Implementados

El sistema ahora valida que los siguientes campos **NO SE REPITAN** entre diferentes pólizas:

### 1. **Número de Póliza** 📄
- **Campo:** `numero_poliza`
- **Descripción:** Cada número de póliza debe ser único en el sistema
- **Validación:** No se permite crear o modificar una póliza con un número que ya existe

### 2. **Endoso** 📝
- **Campo:** `endoso`
- **Descripción:** El número de endoso debe ser único
- **Validación:** No se permite duplicar números de endoso

### 3. **Inciso** 📊
- **Campo:** `inciso`
- **Descripción:** El inciso debe ser único en el sistema
- **Validación:** No se permite duplicar incisos

### 4. **Número de Serie/VIN** 🔢
- **Campo:** `serie_vin`
- **Descripción:** El número de serie del vehículo (VIN) debe ser único
- **Validación:** No se permite registrar el mismo VIN en múltiples pólizas
- **Razón:** Un vehículo (identificado por su VIN) no puede tener múltiples pólizas simultáneas activas

### 5. **Número de Motor** ⚙️
- **Campo:** `motor`
- **Descripción:** El número de motor del vehículo debe ser único
- **Validación:** No se permite duplicar números de motor
- **Razón:** Similar al VIN, cada motor tiene un número único de identificación

---

## ✅ Funcionamiento de las Validaciones

### Al CREAR una nueva póliza (ALTA):

1. El usuario completa el formulario
2. Presiona "Guardar"
3. Confirma la acción en el diálogo
4. **El sistema verifica** que ninguno de los campos únicos esté duplicado
5. Si hay duplicados:
   - ❌ **Muestra un error detallado** indicando:
     - Qué campo está duplicado
     - El valor duplicado
     - La póliza existente que ya tiene ese valor
     - ID y nombre del cliente de la póliza existente
   - La póliza **NO SE CREA**
   - El usuario debe corregir el dato duplicado

6. Si no hay duplicados:
   - ✅ **La póliza se crea exitosamente**

### Al ACTUALIZAR una póliza existente (CAMBIO):

1. El usuario selecciona una póliza de la lista
2. Modifica los datos
3. Presiona "Guardar"
4. Confirma la actualización
5. **El sistema verifica** que los campos únicos no estén duplicados en **OTRAS** pólizas
   - ⚠️ **Importante:** Permite que la póliza mantenga sus propios valores actuales
   - Solo valida contra otras pólizas diferentes
6. Si hay duplicados en otras pólizas:
   - ❌ **Muestra un error detallado**
   - La póliza **NO SE ACTUALIZA**
7. Si no hay duplicados:
   - ✅ **La póliza se actualiza exitosamente**

---

## 💡 Ejemplos de Uso

### ✅ Ejemplo 1: Creación Exitosa
```
Cliente: Juan Pérez
Número de Póliza: POL-2025-001
Serie VIN: 1HGBH41JXMN109186
Motor: E123456789

→ Si estos valores NO EXISTEN en el sistema
→ ✅ Póliza creada exitosamente
```

### ❌ Ejemplo 2: Error por Duplicado
```
Cliente: María López
Número de Póliza: POL-2025-001  ← Ya existe
Serie VIN: 1HGBH41JXMN109999
Motor: E987654321

→ Al intentar guardar:
❌ Error:
"Número de Póliza 'POL-2025-001' ya está registrado

Póliza existente:
• ID: 5
• Cliente: Juan Pérez

Por favor, verifique los datos."

→ La póliza NO SE CREA
→ El usuario debe cambiar el número de póliza
```

### ✅ Ejemplo 3: Actualización Exitosa
```
Póliza ID: 5 (Juan Pérez)
Modificación: Cambiar prima de $5,000 a $6,000
Número de Póliza: POL-2025-001 (sin cambios)

→ Aunque POL-2025-001 ya existe, es de la MISMA póliza
→ ✅ Actualización exitosa
```

### ❌ Ejemplo 4: Error al Actualizar
```
Póliza ID: 5 (Juan Pérez)
Modificación: Cambiar Número de Póliza a POL-2025-002
Pero POL-2025-002 ya pertenece a otra póliza (ID: 7, María López)

→ Al intentar guardar:
❌ Error:
"Número de Póliza 'POL-2025-002' ya está registrado

Póliza existente:
• ID: 7
• Cliente: María López

Por favor, verifique los datos."

→ La póliza NO SE ACTUALIZA
```

---

## 🎯 Campos que PUEDEN Dejarse Vacíos

**Importante:** La validación de unicidad solo se aplica si el campo **TIENE VALOR**.

Si un campo está **vacío o en blanco**:
- ✅ **NO se valida**
- ✅ Múltiples pólizas pueden tener el campo vacío
- ✅ Solo se valida cuando se ingresa un valor

**Ejemplo:**
```
Póliza 1: Endoso = "" (vacío)  ← Permitido
Póliza 2: Endoso = "" (vacío)  ← Permitido
Póliza 3: Endoso = "END-001"   ← Permitido
Póliza 4: Endoso = "END-001"   ← ❌ NO PERMITIDO (duplicado)
```

---

## 🔍 Mensajes de Error

### Formato del Mensaje:
```
❌ [Campo] '[Valor]' ya está registrado

Póliza existente:
• ID: [ID]
• Cliente: [Nombre Completo]

Por favor, verifique los datos.
```

### Ejemplos Reales:

#### Error en Número de Póliza:
```
❌ Número de Póliza 'ABC-123-456' ya está registrado

Póliza existente:
• ID: 15
• Cliente: Carlos Rodríguez

Por favor, verifique los datos.
```

#### Error en VIN:
```
❌ Número de Serie/VIN '1HGBH41JXMN109186' ya está registrado

Póliza existente:
• ID: 8
• Cliente: Ana Martínez

Por favor, verifique los datos.
```

#### Error en Motor:
```
❌ Número de Motor 'E123456789' ya está registrado

Póliza existente:
• ID: 22
• Cliente: Luis Hernández

Por favor, verifique los datos.
```

---

## 🛠️ Implementación Técnica

### Método de Validación:
```python
_validar_campos_unicos(datos: Dict, poliza_id: int = None) -> tuple
```

**Parámetros:**
- `datos`: Diccionario con los datos de la póliza
- `poliza_id`: ID de la póliza (None para nuevas, número para actualización)

**Retorna:**
- `(True, "")` si la validación es exitosa
- `(False, mensaje_error)` si hay campos duplicados

### Campos Validados:
```python
campos_unicos = {
    'numero_poliza': 'Número de Póliza',
    'endoso': 'Endoso',
    'inciso': 'Inciso',
    'serie_vin': 'Número de Serie/VIN',
    'motor': 'Número de Motor'
}
```

### Flujo de Validación:

1. **Para cada campo único:**
   - Verificar si tiene valor
   - Si está vacío → Saltar validación
   - Si tiene valor → Buscar en la base de datos

2. **Búsqueda en base de datos:**
   - **Nueva póliza:** Buscar cualquier coincidencia
   - **Actualización:** Buscar coincidencias excluyendo la póliza actual

3. **Si encuentra duplicado:**
   - Obtener ID y nombre del cliente de la póliza existente
   - Generar mensaje de error detallado
   - Retornar `(False, mensaje)`

4. **Si NO encuentra duplicado:**
   - Continuar con el siguiente campo
   - Si todos los campos son únicos → Retornar `(True, "")`

### Integración con CRUD:

#### En `agregar_poliza()`:
```python
# Validar campos únicos
es_valido, mensaje_error = self._validar_campos_unicos(datos)
if not es_valido:
    raise ValueError(mensaje_error)
# ... continuar con INSERT
```

#### En `actualizar_poliza()`:
```python
# Validar campos únicos (excluyendo la póliza actual)
es_valido, mensaje_error = self._validar_campos_unicos(datos, poliza_id)
if not es_valido:
    raise ValueError(mensaje_error)
# ... continuar con UPDATE
```

---

## 🚨 Casos Especiales

### Caso 1: Actualización sin cambiar campos únicos
✅ **Permitido:** Si actualiza otros campos (prima, fechas, etc.) sin tocar los campos únicos, la validación pasa exitosamente.

### Caso 2: Pólizas antiguas antes de la validación
✅ **Compatible:** Si ya existen pólizas duplicadas de antes, el sistema:
- No las modifica automáticamente
- Previene nuevos duplicados
- Permite actualizar pólizas existentes si no generan nuevos duplicados

### Caso 3: Cambio de mayúsculas/minúsculas
⚠️ **Sensible:** La validación es sensible a mayúsculas/minúsculas
```
"POL-001" ≠ "pol-001"  → Se permiten ambos
```

### Caso 4: Espacios en blanco
✅ **Se eliminan:** Los espacios antes y después se eliminan automáticamente
```
" POL-001 " → Se convierte en "POL-001"
```

---

## 📊 Beneficios del Sistema

### 1. **Integridad de Datos** 🛡️
- Evita registros duplicados
- Mantiene la unicidad de identificadores críticos
- Previene errores de captura

### 2. **Cumplimiento Normativo** ⚖️
- Los números de póliza, VIN y motor son únicos por ley
- El sistema garantiza el cumplimiento automáticamente

### 3. **Facilidad de Búsqueda** 🔍
- Al ser únicos, permiten búsquedas precisas
- No hay ambigüedad en identificadores

### 4. **Auditoría y Trazabilidad** 📈
- Cada vehículo (VIN) tiene una sola póliza activa
- Fácil rastreo de historial

### 5. **Experiencia de Usuario** 👥
- Mensajes de error claros y descriptivos
- Indica exactamente qué dato está duplicado
- Muestra la póliza existente para verificación

---

## 🔄 Flujo Completo de Validación

```
┌─────────────────────────────────────┐
│  Usuario completa formulario        │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Usuario presiona "Guardar"         │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Sistema muestra confirmación       │
│  (ALTA o CAMBIO)                    │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Usuario confirma acción            │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  Validar campos requeridos          │
│  (nombre, prima, RFC, etc.)         │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│  VALIDAR CAMPOS ÚNICOS              │
│  · Número de Póliza                 │
│  · Endoso                           │
│  · Inciso                           │
│  · VIN                              │
│  · Motor                            │
└────────────┬────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
┌──────────┐  ┌──────────────────────┐
│Duplicado?│  │  Campos únicos OK    │
└────┬─────┘  └──────────┬───────────┘
     │                   │
     │ SÍ                │ NO
     │                   │
     ▼                   ▼
┌────────────────┐  ┌──────────────────┐
│ ❌ Mostrar     │  │ ✅ Guardar en DB │
│    error       │  │                  │
│    detallado   │  └────────┬─────────┘
│                │           │
│ · Qué campo    │           ▼
│ · Qué valor    │  ┌──────────────────┐
│ · Póliza       │  │ ✅ Mensaje éxito │
│   existente    │  │                  │
└────────────────┘  │ Recargar lista   │
                    │ Limpiar form     │
                    └──────────────────┘
```

---

## 💻 Código de Ejemplo

### Crear una Póliza:
```python
datos = {
    'nombre_completo': 'Juan Pérez',
    'numero_poliza': 'POL-2025-001',
    'serie_vin': '1HGBH41JXMN109186',
    'motor': 'E123456789',
    # ... otros campos
}

try:
    poliza_id = db.agregar_poliza(datos)
    print(f"✅ Póliza creada con ID: {poliza_id}")
except ValueError as e:
    print(f"❌ Error: {e}")
```

### Actualizar una Póliza:
```python
poliza_id = 5
datos = {
    'nombre_completo': 'Juan Pérez García',
    'numero_poliza': 'POL-2025-001',  # Sin cambios
    'prima_total': 6000.00,  # Cambiado
    # ... otros campos
}

try:
    exito = db.actualizar_poliza(poliza_id, datos)
    if exito:
        print("✅ Póliza actualizada")
except ValueError as e:
    print(f"❌ Error: {e}")
```

---

## 📝 Notas Importantes

1. ✅ **Los campos vacíos NO se validan** (múltiples pólizas pueden tener campos vacíos)
2. ✅ **La validación es automática** (no requiere acción del usuario)
3. ✅ **Los mensajes son descriptivos** (incluyen la póliza existente)
4. ✅ **Compatible con datos existentes** (no afecta pólizas creadas antes)
5. ✅ **Previene errores humanos** (alertas tempranas de duplicados)

---

## 🎓 Recomendaciones

### Para Usuarios:
1. **Verificar datos antes de guardar** para evitar errores
2. **Revisar el mensaje de error** si aparece duplicado
3. **Consultar la póliza existente** mencionada en el error
4. **Corregir el dato duplicado** antes de reintentar

### Para Administradores:
1. **Capacitar a usuarios** sobre campos únicos
2. **Revisar periódicamente** que no haya duplicados antiguos
3. **Establecer nomenclaturas** para números de póliza
4. **Documentar procesos** de asignación de números

---

## 📞 Soporte

Si tiene preguntas sobre las validaciones de campos únicos, consulte este documento o contacte al administrador del sistema.

**Sistema:** ASEGURANZA v2.1
**Módulo:** database.py - Validación de Campos Únicos
**Última actualización:** Marzo 2026

---

**🔒 Sistema de validación de campos únicos implementado exitosamente**
