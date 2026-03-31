# 🎨 PALETA DE COLORES - ASEGURANZA

## 📋 COLORES CORPORATIVOS

### 🔵 Colores Primarios
```python
"primario": "#1e3a8a"           # Azul oscuro corporativo
"primario_hover": "#1e40af"     # Azul oscuro hover
"secundario": "#3b82f6"         # Azul brillante
```

**Uso:**
- Headers principales
- Sección "Datos de Póliza"
- Botón Exportar

**Vista previa:**
```
████████  #1e3a8a  Primario
████████  #1e40af  Primario Hover
████████  #3b82f6  Secundario
```

---

### 🟢 Colores de Éxito
```python
"exito": "#10b981"              # Verde éxito
"exito_hover": "#059669"        # Verde éxito hover
```

**Uso:**
- Botón "Guardar Póliza"
- Botón "Nueva Póliza"
- Estados positivos

**Vista previa:**
```
████████  #10b981  Éxito
████████  #059669  Éxito Hover
```

---

### 🔴 Colores de Peligro
```python
"peligro": "#dc2626"            # Rojo peligro
"peligro_hover": "#b91c1c"      # Rojo peligro hover
```

**Uso:**
- Botón "Eliminar Póliza"
- Alertas de vencimiento
- Pólizas próximas a vencer (< 15 días)

**Vista previa:**
```
████████  #dc2626  Peligro
████████  #b91c1c  Peligro Hover
```

---

### 🟡 Color de Advertencia
```python
"advertencia": "#f59e0b"        # Amarillo advertencia
```

**Uso:**
- Sección "Datos del Vehículo"
- Notificaciones importantes

**Vista previa:**
```
████████  #f59e0b  Advertencia
```

---

### 🔵 Color de Información
```python
"info": "#06b6d4"               # Cyan información
```

**Uso:**
- Sección "Información Personal"
- Datos informativos

**Vista previa:**
```
████████  #06b6d4  Información
```

---

### ⚫ Colores de Fondo
```python
"fondo_oscuro": "#1e293b"       # Fondo principal oscuro
"fondo_claro": "#334155"        # Fondo paneles
"borde": "#475569"              # Bordes y separadores
```

**Uso:**
- Fondo general de la aplicación
- Paneles izquierdo y derecho
- Líneas separadoras

**Vista previa:**
```
████████  #1e293b  Fondo Oscuro
████████  #334155  Fondo Claro
████████  #475569  Bordes
```

---

### ⚪ Colores de Texto
```python
"texto": "#f1f5f9"              # Texto principal (blanco-gris)
"texto_secundario": "#cbd5e1"   # Texto secundario (gris claro)
```

**Uso:**
- Etiquetas de campos
- Títulos y subtítulos
- Texto general

**Vista previa:**
```
████████  #f1f5f9  Texto Principal
████████  #cbd5e1  Texto Secundario
```

---

## 🎯 APLICACIÓN POR COMPONENTE

### Header Principal
```
╔══════════════════════════════════╗
║ Fondo: #1e3a8a (Primario)        ║
║ Texto: #ffffff (Blanco)          ║
║ Altura: 90px                     ║
║ Bordes redondeados: 12px         ║
╚══════════════════════════════════╝
```

### Panel Izquierdo
```
┌──────────────────────────────────┐
│ Fondo: #334155 (Fondo Claro)    │
│ Borde: #475569                   │
│ Ancho: 420px                     │
│ Bordes redondeados: 10px         │
└──────────────────────────────────┘
```

### Header de Búsqueda
```
┌──────────────────────────────────┐
│ Texto: "🔍 BÚSQUEDA DE PÓLIZAS" │
│ Fondo: #3b82f6 (Secundario)     │
│ Color texto: #ffffff             │
│ Altura: 50px                     │
└──────────────────────────────────┘
```

### Campo de Búsqueda
```
┌──────────────────────────────────┐
│ Altura: 45px                     │
│ Borde: #475569 (2px)             │
│ Esquinas: 10px                   │
│ Placeholder: #94a3b8             │
└──────────────────────────────────┘
```

### Botón Nueva Póliza
```
┌──────────────────────────────────┐
│ Fondo: #10b981 (Éxito)           │
│ Hover: #059669 (Éxito Hover)     │
│ Texto: #ffffff                   │
│ Altura: 50px                     │
│ Esquinas: 10px                   │
└──────────────────────────────────┘
```

### Items de Póliza (Normal)
```
┌──────────────────────────────────┐
│ Fondo: #334155                   │
│ Hover: #475569                   │
│ Borde: #475569 (2px)             │
│ Esquinas: 10px                   │
│ Altura: 70px                     │
└──────────────────────────────────┘
```

### Items de Póliza (Vencimiento Próximo)
```
┌──────────────────────────────────┐
│ Fondo: #dc2626 (Peligro)         │
│ Hover: #b91c1c (Peligro Hover)   │
│ Borde: #ef4444 (2px)             │
│ Icono: ⚠️ (warning)              │
│ Esquinas: 10px                   │
└──────────────────────────────────┘
```

### Panel Derecho
```
┌──────────────────────────────────┐
│ Fondo: #334155 (Fondo Claro)    │
│ Borde: #475569 (1px)             │
│ Bordes redondeados: 10px         │
└──────────────────────────────────┘
```

### Header del Formulario
```
┌──────────────────────────────────┐
│ Fondo: #3b82f6 (Secundario)     │
│ Texto título: #ffffff            │
│ Texto subtítulo: #cbd5e1         │
│ Altura: 70px                     │
│ Esquinas: 10px                   │
└──────────────────────────────────┘
```

### Secciones del Formulario
```
Información Personal:
████████  #06b6d4 (Info)

Datos de Póliza:
████████  #3b82f6 (Secundario)

Datos del Vehículo:
████████  #f59e0b (Advertencia)
```

### Campos de Entrada
```
┌──────────────────────────────────┐
│ Altura: 40px                     │
│ Borde: #475569 (2px)             │
│ Esquinas: 8px                    │
│ Font: 13px                       │
└──────────────────────────────────┘
```

### Etiquetas de Campos
```
Texto: "Campo Label"
Color: #f1f5f9 (Texto)
Font: 11px bold
```

### Botones de Acción

**Guardar:**
```
┌──────────────────────────────────┐
│ Fondo: #10b981 (Éxito)           │
│ Hover: #059669                   │
│ Texto: #ffffff (Blanco)          │
│ Texto: "💾 GUARDAR PÓLIZA"       │
│ Altura: 50px                     │
│ Esquinas: 10px                   │
└──────────────────────────────────┘
```

**Cancelar:**
```
┌──────────────────────────────────┐
│ Fondo: #64748b (Gris)            │
│ Hover: #475569                   │
│ Texto: #ffffff                   │
│ Texto: "❌ CANCELAR"             │
│ Altura: 50px                     │
└──────────────────────────────────┘
```

**Exportar:**
```
┌──────────────────────────────────┐
│ Fondo: #3b82f6 (Secundario)      │
│ Hover: #1e40af                   │
│ Texto: #ffffff                   │
│ Texto: "📊 EXPORTAR A EXCEL"     │
│ Altura: 50px                     │
└──────────────────────────────────┘
```

**Eliminar:**
```
┌──────────────────────────────────┐
│ Fondo: #dc2626 (Peligro)         │
│ Hover: #b91c1c                   │
│ Texto: #ffffff                   │
│ Texto: "🗑️ ELIMINAR PÓLIZA"     │
│ Altura: 50px                     │
└──────────────────────────────────┘
```

### Footer
```
╔══════════════════════════════════╗
║ Fondo: #1e293b (Fondo Oscuro)   ║
║ Texto: #94a3b8                   ║
║ Estado: 🟢 #10b981 (Éxito)       ║
║ Altura: 50px                     ║
║ Bordes redondeados: 10px         ║
╚══════════════════════════════════╝
```

---

## 🔧 CÓDIGO DE REFERENCIA

### Diccionario de Colores (main.py)
```python
COLORES = {
    # Colores primarios
    "primario": "#1e3a8a",           # Azul oscuro corporativo
    "primario_hover": "#1e40af",     # Azul oscuro hover
    "secundario": "#3b82f6",         # Azul brillante
    
    # Colores de estado
    "exito": "#10b981",              # Verde
    "exito_hover": "#059669",        # Verde hover
    "peligro": "#dc2626",            # Rojo
    "peligro_hover": "#b91c1c",      # Rojo hover
    "advertencia": "#f59e0b",        # Amarillo
    "info": "#06b6d4",               # Cyan
    
    # Colores de fondo
    "fondo_oscuro": "#1e293b",       # Fondo principal
    "fondo_claro": "#334155",        # Paneles
    "borde": "#475569",              # Bordes
    
    # Colores de texto
    "texto": "#f1f5f9",              # Texto principal
    "texto_secundario": "#cbd5e1"    # Texto secundario
}
```

---

## 📐 MEDIDAS ESTÁNDAR

### Alturas
- Header principal: 90px
- Header sección: 50px
- Header formulario: 70px
- Campos entrada: 40px
- Botones búsqueda: 45px
- Botones acción: 50px
- Items lista: 70px
- Footer: 50px

### Espaciados
- Padding externo: 15px
- Padding headers: 20px (horizontal), 10px (vertical)
- Margen entre filas: 5px
- Margen entre columnas: 10px
- Margen secciones: 20px (arriba), 15px (abajo)

### Bordes
- Grosor estándar: 2px
- Grosor delgado: 1px
- Radio esquinas principales: 10-12px
- Radio esquinas campos: 8px

---

## 💾 EXPORTAR

Este archivo puede servir como guía para:
- Mantener consistencia visual
- Crear nuevas funcionalidades
- Documentar el diseño
- Trasladar a otras plataformas
- Crear versiones web/móvil

**Fecha:** Enero 2024
**Sistema:** ASEGURANZA
**Framework:** CustomTkinter
