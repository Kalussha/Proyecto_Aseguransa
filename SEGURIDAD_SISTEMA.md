# 🔐 SISTEMA DE SEGURIDAD - ASEGURANZA

## CREDENCIALES POR DEFECTO

**Usuario:** `admin`  
**Contraseña:** `admin123`

---

## FUNCIONALIDADES DE SEGURIDAD IMPLEMENTADAS

### 1. Sistema de Login (Autenticación)
✓ **Ventana de inicio de sesión** al abrir la aplicación
✓ **Validación de credenciales** contra base de datos
✓ **Contraseña encriptada** con SHA-256
✓ **Mensaje de error** si las credenciales son incorrectas
✓ **Usuario mostrado** en el header de la aplicación

### 2. Confirmaciones de Acciones

#### ✅ ALTA (Crear Nueva Póliza)
- Se solicita confirmación antes de guardar
- Mensaje: *"¿Está seguro de crear una nueva póliza para: [Nombre]?"*

#### ✅ BAJA (Eliminar Póliza)
- Se solicita confirmación antes de eliminar
- Mensaje: *"¿Estás seguro de que deseas eliminar esta póliza? Esta acción no se puede deshacer."*

#### ✅ CAMBIO (Actualizar Póliza)
- Se solicita confirmación antes de actualizar
- Mensaje: *"¿Está seguro de actualizar la póliza de: [Nombre]? Esta acción modificará los datos existentes."*

---

## TABLA DE USUARIOS EN LA BASE DE DATOS

La tabla `usuarios` contiene:
- `id` - Identificador único
- `usuario` - Nombre de usuario (único)
- `password_hash` - Contraseña encriptada SHA-256
- `nombre_completo` - Nombre completo del usuario
- `activo` - Estado del usuario (1 = activo, 0 = inactivo)
- `fecha_creacion` - Fecha de creación del usuario

---

## MÉTODOS DISPONIBLES EN DatabaseManager

### `verificar_credenciales(usuario, password)`
Valida usuario y contraseña. Retorna datos del usuario si son correctas.

**Ejemplo:**
```python
usuario_data = db.verificar_credenciales("admin", "admin123")
if usuario_data:
    print(f"Bienvenido {usuario_data['nombre_completo']}")
```

### `agregar_usuario(usuario, password, nombre_completo)`
Crea un nuevo usuario en el sistema.

**Ejemplo:**
```python
db.agregar_usuario("juan", "mipass123", "Juan Pérez")
```

### `cambiar_password(usuario, password_actual, password_nuevo)`
Cambia la contraseña de un usuario existente.

**Ejemplo:**
```python
db.cambiar_password("admin", "admin123", "nuevapass456")
```

---

## CÓMO AGREGAR MÁS USUARIOS

### Opción 1: Por código Python
```python
from database import DatabaseManager

db = DatabaseManager()
db.agregar_usuario(
    usuario="jose",
    password="jose2026",
    nombre_completo="José García"
)
```

### Opción 2: Directamente en SQLite
```sql
INSERT INTO usuarios (usuario, password_hash, nombre_completo, activo)
VALUES ('maria', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', 'María López', 1);
```
*Nota: El password_hash mostrado corresponde a "password" encriptado con SHA-256*

### Opción 3: Generar hash de contraseña
```python
import hashlib

password = "mipassword"
password_hash = hashlib.sha256(password.encode()).hexdigest()
print(password_hash)
```

---

## FLUJO DE AUTENTICACIÓN

1. **Usuario abre la aplicación** → Aparece ventana de login
2. **Ingresa credenciales** → Se validan contra la base de datos
3. **Credenciales correctas** → Se cierra login y abre aplicación principal
4. **Credenciales incorrectas** → Muestra error y permite reintentar
5. **Usuario mostrado en header** → Indica quién está usando el sistema

---

## SEGURIDAD IMPLEMENTADA

✓ **Contraseñas encriptadas** - Se usa SHA-256 (hash de 64 caracteres)
✓ **No se guardan contraseñas en texto plano**
✓ **Validación de usuarios activos** - Solo usuarios con `activo=1` pueden entrar
✓ **Ventana modal** - El login es obligatorio, no se puede cerrar sin autenticarse
✓ **Confirmaciones obligatorias** - Previene acciones accidentales
✓ **Trazabilidad** - Se puede saber qué usuario está operando

---

## MEJORAS FUTURAS SUGERIDAS

### Nivel Básico
- [ ] Botón "Cerrar Sesión" en el header
- [ ] Límite de intentos fallidos de login
- [ ] Recordar último usuario usado

### Nivel Intermedio
- [ ] Registro de auditoría (quién hizo qué y cuándo)
- [ ] Niveles de permisos (admin, operador, consulta)
- [ ] Cambio de contraseña desde la aplicación
- [ ] Gestión de usuarios desde la interfaz

### Nivel Avanzado
- [ ] Autenticación de dos factores (2FA)
- [ ] Sesiones con timeout automático
- [ ] Recuperación de contraseña por email
- [ ] Bloqueo de cuenta después de X intentos

---

## SOLUCIÓN DE PROBLEMAS

### "No puedo entrar con admin/admin123"
**Solución:** Verifica que hayas escrito correctamente. El usuario y contraseña son sensibles a mayúsculas/minúsculas.

### "Olvidé mi contraseña"
**Solución:** Puedes resetear la contraseña directamente en la base de datos:
```python
import hashlib
from database import DatabaseManager

db = DatabaseManager()
nueva_pass = hashlib.sha256("nuevapass".encode()).hexdigest()

# Conectar y actualizar
conn = db.get_connection()
cursor = conn.cursor()
cursor.execute("UPDATE usuarios SET password_hash = ? WHERE usuario = 'admin'", (nueva_pass,))
conn.commit()
conn.close()
```

### "Quiero eliminar el login temporalmente"
**Solución:** Comenta estas líneas en `main.py`:
```python
# if __name__ == "__main__":
#     root = ctk.CTk()
#     root.withdraw()
#     db = DatabaseManager()
#     login = LoginWindow(root, db)
#     root.wait_window(login)
#     
#     if login.usuario_autenticado:
#         root.destroy()
#         app = SeguroApp(usuario_autenticado=login.usuario_autenticado)
#         app.mainloop()

# Y descomenta esto:
if __name__ == "__main__":
    app = SeguroApp()  # Sin usuario
    app.mainloop()
```

---

## HASH SHA-256 DE CONTRASEÑAS COMUNES

Para referencia rápida:

| Contraseña | Hash SHA-256 |
|------------|--------------|
| admin123 | 240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9 |
| password | 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 |
| 12345678 | ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f |

---

**Fecha de implementación:** 09/03/2026  
**Versión del sistema:** 1.0.0  
**Estado:** ✅ Implementado y funcionando
