# 📘 Manual de Gestión de Usuarios - ASEGURNASA

## 🔐 Sistema de Autenticación y Gestión de Usuarios

### Índice
1. [Inicio de Sesión](#inicio-de-sesión)
2. [Cambio de Contraseña Obligatorio](#cambio-de-contraseña-obligatorio)
3. [Gestión de Usuarios (Solo Admin)](#gestión-de-usuarios-solo-admin)
4. [Cambio de Contraseña Voluntario](#cambio-de-contraseña-voluntario)
5. [Configuración de Email](#configuración-de-email)
6. [Seguridad del Sistema](#seguridad-del-sistema)

---

## 🚪 Inicio de Sesión

### Credenciales por Defecto
Al iniciar el sistema por primera vez, utilice las siguientes credenciales:

- **Usuario:** `admin`
- **Contraseña:** `admin123`

⚠️ **IMPORTANTE:** El sistema le solicitará cambiar esta contraseña al primer inicio de sesión.

### Proceso de Login
1. Ingrese su nombre de usuario
2. Ingrese su contraseña
3. Presione "Iniciar Sesión" o la tecla Enter
4. Si es la primera vez o tiene una contraseña temporal, será redirigido al cambio de contraseña

### Estados de Usuario
- ✅ **Activo:** Puede iniciar sesión normalmente
- ❌ **Inactivo:** No puede iniciar sesión (desactivado por admin)
- ⚠️ **Requiere cambio de contraseña:** Debe cambiar contraseña antes de usar el sistema

---

## 🔑 Cambio de Contraseña Obligatorio

### ¿Cuándo se requiere cambiar la contraseña?

El sistema **fuerza** el cambio de contraseña en los siguientes casos:
1. **Primer inicio de sesión** con el usuario admin por defecto
2. **Usuarios nuevos** creados por el administrador (reciben contraseña temporal)
3. Cuando el administrador **restablece** la contraseña de un usuario

### Proceso de Cambio Obligatorio

1. **Después de iniciar sesión**, aparece la ventana "Cambio de Contraseña Obligatorio"
2. Esta ventana **NO SE PUEDE CERRAR** hasta completar el cambio
3. Complete los siguientes campos:
   - **Contraseña Actual:** La contraseña temporal recibida
   - **Nueva Contraseña:** Su nueva contraseña personal (mínimo 8 caracteres)
   - **Confirmar Nueva Contraseña:** Repita la nueva contraseña

4. Presione "Cambiar Contraseña"
5. Una vez cambiada exitosamente, accederá al sistema normalmente

### Requisitos de Contraseña
- ✔️ Mínimo **8 caracteres**
- ✔️ Se recomienda incluir:
  - Letras mayúsculas y minúsculas
  - Números
  - Símbolos especiales (!@#$%&*)

---

## 👥 Gestión de Usuarios (Solo Admin)

### Acceso
Solo el usuario **admin** puede gestionar usuarios. El botón "👥 Gestión de Usuarios" aparece en el header superior derecho.

### Crear Nuevo Usuario

1. Click en "➕ Crear Nuevo Usuario"
2. Complete el formulario:
   - **Usuario:** Nombre único de inicio de sesión (obligatorio)
   - **Nombre Completo:** Nombre y apellidos del usuario (obligatorio)
   - **Email:** Correo electrónico (opcional, necesario para envío automático)

3. **Configuración de Email (Opcional):**
   - Si desea enviar la contraseña temporal por email, complete:
     - **Email Remitente:** Su cuenta de Gmail
     - **Contraseña App de Gmail:** Contraseña de aplicación de Google
   - Si no configura email, la contraseña aparecerá en pantalla para copiarla manualmente

4. Click en "Crear Usuario"
   - El sistema genera una **contraseña temporal aleatoria** de 12 caracteres
   - Si configuró email, se enviará automáticamente al usuario
   - Si no, aparecerá un mensaje mostrando la contraseña (¡CÓPIELA!)

### Contraseñas Temporales Generadas
Las contraseñas temporales son:
- ✅ **12 caracteres** de longitud
- ✅ Incluyen letras (mayúsculas y minúsculas), números y símbolos
- ✅ Generadas con algoritmos criptográficos seguros
- ✅ Ejemplo: `aB3!xY9@mK2$`

### Activar/Desactivar Usuarios

#### Desactivar Usuario
1. En la lista de usuarios, click en "Desactivar" del usuario deseado
2. Confirme la acción
3. El usuario **no podrá iniciar sesión** hasta ser reactivado

#### Activar Usuario
1. En la lista de usuarios, click en "Activar" del usuario desactivado
2. El usuario puede iniciar sesión nuevamente

### Lista de Usuarios
La ventana de gestión muestra:
- 👤 **Nombre completo** del usuario
- **Usuario** de inicio de sesión
- 📧 **Email** (si fue proporcionado)
- **Badges de estado:**
  - ✅ **Activo** (verde) / ❌ **Inactivo** (rojo)
  - ⚠️ **Debe cambiar contraseña** (amarillo)

---

## 🔒 Cambio de Contraseña Voluntario

Cualquier usuario puede cambiar su contraseña en cualquier momento.

### Proceso
1. Click en "🔑 Cambiar Contraseña" en el header superior derecho
2. Complete el formulario:
   - **Contraseña Actual:** Su contraseña actual
   - **Nueva Contraseña:** La nueva contraseña deseada (mínimo 8 caracteres)
   - **Confirmar Nueva Contraseña:** Repita la nueva contraseña

3. Click en "Cambiar Contraseña" o presione Enter
4. La contraseña se cambia inmediatamente
5. Puede hacer click en "Cancelar" si no desea cambiarla

---

## 📧 Configuración de Email

### Configurar Gmail para Envío de Contraseñas

Para que el sistema pueda enviar emails con contraseñas temporales:

#### 1. Crear Contraseña de Aplicación en Google

1. Vaya a su **Cuenta de Google**: https://myaccount.google.com
2. Seleccione **Seguridad** → **Verificación en dos pasos** (debe estar activada)
3. Vaya a **Contraseñas de aplicaciones**
4. Seleccione "Correo" y "Windows Computer" (o el dispositivo que use)
5. Google generará una contraseña de 16 caracteres (ejemplo: `abcd efgh ijkl mnop`)
6. **COPIE ESTA CONTRASEÑA** (la necesitará en el sistema)

#### 2. Configurar en ASEGURNASA

Al crear un usuario:
- **Email Remitente:** su_correo@gmail.com
- **Contraseña App de Gmail:** La contraseña de 16 caracteres generada

#### 3. Formato del Email Enviado

Los usuarios recibirán un email profesional con:
- 📌 Logo y branding de ASEGURNASA
- 📦 Credenciales en un cuadro amarillo destacado:
  - Usuario
  - Contraseña temporal
- ⚠️ Advertencias de seguridad en cuadro rojo:
  - Cambiar contraseña inmediatamente
  - No compartir credenciales
  - Proteger el email

### Consideraciones de Seguridad
- ⚠️ **NO use su contraseña principal de Gmail** en el sistema
- ✅ Use una **contraseña de aplicación** específica
- ✅ Puede revocar la contraseña desde Google en cualquier momento
- ✅ Si no configura email, puede entregar la contraseña manualmente

---

## 🛡️ Seguridad del Sistema

### Encriptación de Contraseñas
- Todas las contraseñas se almacenan usando **SHA-256**
- El sistema **NUNCA** almacena contraseñas en texto plano
- Ni siquiera el administrador puede ver las contraseñas de los usuarios

### Protección contra Acceso No Autorizado
- ✅ Login obligatorio para acceder al sistema
- ✅ Contraseñas temporales fuerzan cambio inmediato
- ✅ Usuarios inactivos no pueden iniciar sesión
- ✅ Contraseñas deben tener mínimo 8 caracteres

### Auditoría y Rastreo
El sistema registra:
- 📅 **Fecha de creación** del usuario
- 🕐 **Último cambio de contraseña**
- ⚠️ **Estado de contraseña temporal** (si debe cambiarla)

### Recuperación de Contraseñas
Si un usuario olvida su contraseña:
1. Contactar al **administrador** del sistema
2. El admin puede **desactivar y reactivar** al usuario (esto generará nueva contraseña temporal)
3. O el admin puede **crear un nuevo usuario** con las mismas credenciales

---

## 📋 Flujo Completo de Usuario Nuevo

### Para el Administrador:
1. Login como admin
2. Click en "👥 Gestión de Usuarios"
3. Click en "➕ Crear Nuevo Usuario"
4. Completar formulario (usuario, nombre, email)
5. Configurar email (opcional)
6. Click en "Crear Usuario"
7. Copiar contraseña temporal (si no se envió por email)
8. Entregar credenciales al usuario

### Para el Usuario Nuevo:
1. Recibir credenciales del administrador:
   - Por **email** (si fue configurado)
   - Por **mensaje directo** (si no hay email)

2. Iniciar sesión en ASEGURNASA:
   - Usuario: [su_usuario]
   - Contraseña: [contraseña_temporal]

3. **Cambio de contraseña obligatorio:**
   - Se abre automáticamente ventana de cambio
   - Ingresar contraseña temporal
   - Definir nueva contraseña personal (mínimo 8 caracteres)
   - Confirmar nueva contraseña

4. Acceso al sistema:
   - Una vez cambiada la contraseña, puede usar el sistema normalmente

---

## 🔧 Solución de Problemas

### ❌ "Usuario o contraseña incorrectos"
- Verifique que el usuario esté escrito correctamente
- Verifique que la contraseña esté escrita correctamente (distingue mayúsculas)
- Si es usuario nuevo, asegúrese de usar la contraseña temporal recibida

### ❌ "La nueva contraseña debe tener al menos 8 caracteres"
- Su nueva contraseña debe tener mínimo 8 caracteres
- Intente con una contraseña más larga

### ❌ "La nueva contraseña y su confirmación no coinciden"
- Ambos campos deben ser idénticos
- Vuelva a escribir la confirmación cuidadosamente

### ❌ "Error al enviar email"
- Verifique su conexión a Internet
- Verifique que el email remitente sea correcto
- Verifique que la contraseña de aplicación sea correcta
- Asegúrese de haber activado la verificación en dos pasos en Google

### ⚠️ Usuario desactivado no puede iniciar sesión
- Contacte al administrador para que reactive su cuenta

---

## 📞 Soporte

Para asistencia adicional, contacte al administrador del sistema.

**Sistema:** ASEGURNASA v2.0
**Última actualización:** Enero 2025

---

## 📝 Notas Importantes

1. ⚠️ **Cambie la contraseña del admin** inmediatamente al primer uso
2. ⚠️ **No comparta** sus credenciales con nadie
3. ⚠️ **Use contraseñas seguras** (letras, números, símbolos)
4. ⚠️ **Cambie su contraseña periódicamente** (cada 3-6 meses recomendado)
5. ⚠️ Si configura email, use **contraseña de aplicación** de Google, no su contraseña principal

---

**🚀 ¡Sistema de gestión de usuarios implementado exitosamente!**
