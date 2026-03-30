"""
Módulo de gestión de base de datos SQLite para el sistema de pólizas de seguros.
"""
import sqlite3
import hashlib
import secrets
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class DatabaseManager:
    """Gestiona todas las operaciones de base de datos."""
    
    def __init__(self, db_name: str = "seguros.db"):
        """Inicializa la conexión a la base de datos."""
        self.db_name = db_name
        self.create_tables()
    
    def get_connection(self):
        """Crea y retorna una conexión a la base de datos."""
        return sqlite3.connect(self.db_name)
    
    def _migrate_usuarios_table(self, cursor):
        """Migra la tabla usuarios agregando columnas nuevas si no existen."""
        # Obtener columnas existentes
        cursor.execute("PRAGMA table_info(usuarios)")
        columnas_existentes = [col[1] for col in cursor.fetchall()]
        
        # Columnas que deben existir
        columnas_requeridas = {
            'email': "ALTER TABLE usuarios ADD COLUMN email TEXT",
            'activo': "ALTER TABLE usuarios ADD COLUMN activo INTEGER DEFAULT 1",
            'cambiar_password': "ALTER TABLE usuarios ADD COLUMN cambiar_password INTEGER DEFAULT 1",
            'password_temporal': "ALTER TABLE usuarios ADD COLUMN password_temporal INTEGER DEFAULT 0",
            'fecha_creacion': "ALTER TABLE usuarios ADD COLUMN fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP",
            'ultimo_cambio_password': "ALTER TABLE usuarios ADD COLUMN ultimo_cambio_password TEXT"
        }
        
        # Agregar columnas faltantes
        for columna, sql in columnas_requeridas.items():
            if columna not in columnas_existentes:
                try:
                    cursor.execute(sql)
                    print(f"✓ Columna '{columna}' agregada a la tabla usuarios")
                except sqlite3.OperationalError as e:
                    print(f"✗ Error al agregar columna '{columna}': {e}")
    
    def _migrate_polizas_table(self, cursor):
        """Migra la tabla polizas agregando columnas nuevas si no existen."""
        # Obtener columnas existentes
        cursor.execute("PRAGMA table_info(polizas)")
        columnas_existentes = [col[1] for col in cursor.fetchall()]
        
        # Columnas que deben existir (todas las columnas nuevas o que podrían faltar)
        columnas_requeridas = {
            'tipo_moneda': "ALTER TABLE polizas ADD COLUMN tipo_moneda TEXT DEFAULT 'MXN'",
            'uso': "ALTER TABLE polizas ADD COLUMN uso TEXT",
            'servicio': "ALTER TABLE polizas ADD COLUMN servicio TEXT",
            'ultimo_movimiento': "ALTER TABLE polizas ADD COLUMN ultimo_movimiento TEXT",
            'endoso': "ALTER TABLE polizas ADD COLUMN endoso TEXT",
            'inciso': "ALTER TABLE polizas ADD COLUMN inciso TEXT",
            'fecha_vencimiento_pago': "ALTER TABLE polizas ADD COLUMN fecha_vencimiento_pago TEXT",
            'coberturas_json': "ALTER TABLE polizas ADD COLUMN coberturas_json TEXT",
            'comentarios': "ALTER TABLE polizas ADD COLUMN comentarios TEXT",
            'fecha_actualizacion': "ALTER TABLE polizas ADD COLUMN fecha_actualizacion TEXT DEFAULT CURRENT_TIMESTAMP",
            'telefono': "ALTER TABLE polizas ADD COLUMN telefono TEXT"
        }
        
        # Agregar columnas faltantes
        for columna, sql in columnas_requeridas.items():
            if columna not in columnas_existentes:
                try:
                    cursor.execute(sql)
                    print(f"✓ Columna '{columna}' agregada a la tabla polizas")
                except sqlite3.OperationalError as e:
                    print(f"✗ Error al agregar columna '{columna}': {e}")
    
    def create_tables(self):
        """Crea las tablas necesarias si no existen."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                nombre_completo TEXT,
                email TEXT,
                activo INTEGER DEFAULT 1,
                cambiar_password INTEGER DEFAULT 1,
                password_temporal INTEGER DEFAULT 0,
                fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
                ultimo_cambio_password TEXT
            )
        ''')
        
        # Migrar tabla usuarios si es necesaria (agregar columnas nuevas)
        self._migrate_usuarios_table(cursor)
        
        # Tabla de pólizas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS polizas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                -- Bloque 1: Información Personal
                nombre_completo TEXT NOT NULL,
                calle TEXT,
                numero TEXT,
                codigo_postal TEXT,
                colonia TEXT,
                municipio TEXT,
                estado TEXT,
                rfc TEXT,
                email TEXT,
                telefono TEXT,
                
                -- Bloque 2: Datos de Póliza
                compania_aseguradora TEXT,
                numero_poliza TEXT,
                endoso TEXT,
                inciso TEXT,
                vigencia_inicio TEXT,
                vigencia_fin TEXT,
                forma_pago TEXT,
                fecha_vencimiento_pago TEXT,
                tipo_moneda TEXT DEFAULT 'MXN',
                
                -- Bloque 2: Datos del Vehículo
                marca TEXT,
                modelo TEXT,
                tipo_version TEXT,
                anio TEXT,
                serie_vin TEXT,
                motor TEXT,
                placas TEXT,
                uso TEXT,
                servicio TEXT,
                ultimo_movimiento TEXT,
                prima_total REAL,
                
                -- Coberturas (almacenadas como JSON)
                coberturas_json TEXT,
                
                -- Comentarios
                comentarios TEXT,
                
                -- Metadatos
                fecha_creacion TEXT DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Migrar tabla polizas si es necesaria
        self._migrate_polizas_table(cursor)
        
        # Crear usuario por defecto si no existe
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        if cursor.fetchone()[0] == 0:
            # Usuario por defecto: admin / admin123 (debe cambiar contraseña)
            password_hash = hashlib.sha256("admin123".encode()).hexdigest()
            cursor.execute(
                "INSERT INTO usuarios (usuario, password_hash, nombre_completo, cambiar_password, email) VALUES (?, ?, ?, ?, ?)",
                ("admin", password_hash, "Administrador", 1, "admin@asegurnasa.com")
            )
        else:
            # Actualizar usuarios existentes con valores por defecto si las columnas eran NULL
            cursor.execute("""
                UPDATE usuarios 
                SET activo = 1 
                WHERE activo IS NULL
            """)
            cursor.execute("""
                UPDATE usuarios 
                SET cambiar_password = 0 
                WHERE cambiar_password IS NULL
            """)
            cursor.execute("""
                UPDATE usuarios 
                SET password_temporal = 0 
                WHERE password_temporal IS NULL
            """)
        
        conn.commit()
        conn.close()
    
    def _validar_campos_unicos(self, datos: Dict, poliza_id: int = None) -> tuple:
        """
        Valida que los campos únicos no estén duplicados.
        
        Args:
            datos: Diccionario con los datos de la póliza
            poliza_id: ID de la póliza (None para nuevas, número para actualización)
        
        Returns:
            tuple: (es_valido: bool, mensaje_error: str)
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # 1. Validar combinación Póliza + Inciso + Endoso
        numero_poliza = datos.get('numero_poliza', '').strip()
        inciso = datos.get('inciso', '').strip()
        endoso = datos.get('endoso', '').strip()
        
        if numero_poliza:
            if poliza_id:
                cursor.execute(
                    "SELECT id, nombre_completo FROM polizas WHERE numero_poliza = ? AND inciso = ? AND endoso = ? AND id != ?",
                    (numero_poliza, inciso, endoso, poliza_id)
                )
            else:
                cursor.execute(
                    "SELECT id, nombre_completo FROM polizas WHERE numero_poliza = ? AND inciso = ? AND endoso = ?",
                    (numero_poliza, inciso, endoso)
                )
            
            resultado = cursor.fetchone()
            if resultado:
                conn.close()
                poliza_existente_id, nombre_completo = resultado
                
                detalles = f"Póliza: '{numero_poliza}'"
                if inciso:
                    detalles += f", Inciso: '{inciso}'"
                if endoso:
                    detalles += f", Endoso: '{endoso}'"
                    
                mensaje = f"❌ La combinación de {detalles} ya está registrada\n\n"
                mensaje += f"Póliza existente:\n"
                mensaje += f"• ID: {poliza_existente_id}\n"
                mensaje += f"• Cliente: {nombre_completo}\n\n"
                mensaje += f"Por favor, verifique los datos."
                return (False, mensaje)

        # 2. Validar VIN y Motor (estos deben ser únicos por vehículo)
        campos_unicos = {
            'serie_vin': 'Número de Serie/VIN',
            'motor': 'Número de Motor'
        }
        
        for campo_db, campo_nombre in campos_unicos.items():
            valor = datos.get(campo_db, '').strip()
            
            # Solo validar si el campo tiene valor
            if valor:
                # Buscar si ya existe
                if poliza_id:
                    # Al actualizar, excluir la póliza actual
                    cursor.execute(
                        f"SELECT id, nombre_completo FROM polizas WHERE {campo_db} = ? AND id != ?",
                        (valor, poliza_id)
                    )
                else:
                    # Al crear nueva, buscar cualquier coincidencia
                    cursor.execute(
                        f"SELECT id, nombre_completo FROM polizas WHERE {campo_db} = ?",
                        (valor,)
                    )
                
                resultado = cursor.fetchone()
                if resultado:
                    conn.close()
                    poliza_existente_id, nombre_completo = resultado
                    mensaje = f"❌ {campo_nombre} '{valor}' ya está registrado en otra póliza/inciso\n\n"
                    mensaje += f"Póliza existente:\n"
                    mensaje += f"• ID: {poliza_existente_id}\n"
                    mensaje += f"• Cliente: {nombre_completo}\n\n"
                    mensaje += f"Por favor, verifique los datos."
                    return (False, mensaje)
        
        conn.close()
        return (True, "")
    
    def agregar_poliza(self, datos: Dict) -> int:
        """Agrega una nueva póliza a la base de datos."""
        # Validar campos únicos
        es_valido, mensaje_error = self._validar_campos_unicos(datos)
        if not es_valido:
            raise ValueError(mensaje_error)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO polizas (
                nombre_completo, calle, numero, codigo_postal, colonia, municipio, estado,
                rfc, email, telefono, compania_aseguradora, numero_poliza, endoso, inciso,
                vigencia_inicio, vigencia_fin, forma_pago, fecha_vencimiento_pago, tipo_moneda,
                marca, modelo, tipo_version, anio, serie_vin, motor, placas, uso, servicio,
                ultimo_movimiento, prima_total, coberturas_json, comentarios
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            datos.get('nombre_completo', ''),
            datos.get('calle', ''),
            datos.get('numero', ''),
            datos.get('codigo_postal', ''),
            datos.get('colonia', ''),
            datos.get('municipio', ''),
            datos.get('estado', ''),
            datos.get('rfc', ''),
            datos.get('email', ''),
            datos.get('telefono', ''),
            datos.get('compania_aseguradora', ''),
            datos.get('numero_poliza', ''),
            datos.get('endoso', ''),
            datos.get('inciso', ''),
            datos.get('vigencia_inicio', ''),
            datos.get('vigencia_fin', ''),
            datos.get('forma_pago', ''),
            datos.get('fecha_vencimiento_pago', ''),
            datos.get('tipo_moneda', 'MXN'),
            datos.get('marca', ''),
            datos.get('modelo', ''),
            datos.get('tipo_version', ''),
            datos.get('anio', ''),
            datos.get('serie_vin', ''),
            datos.get('motor', ''),
            datos.get('placas', ''),
            datos.get('uso', ''),
            datos.get('servicio', ''),
            datos.get('ultimo_movimiento', ''),
            datos.get('prima_total', 0.0),
            datos.get('coberturas_json', ''),
            datos.get('comentarios', '')
        ))
        
        poliza_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return poliza_id
    
    def actualizar_poliza(self, poliza_id: int, datos: Dict) -> bool:
        """Actualiza una póliza existente."""
        # Validar campos únicos (excluyendo la póliza actual)
        es_valido, mensaje_error = self._validar_campos_unicos(datos, poliza_id)
        if not es_valido:
            raise ValueError(mensaje_error)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE polizas SET
                nombre_completo = ?, calle = ?, numero = ?, codigo_postal = ?,
                colonia = ?, municipio = ?, estado = ?, rfc = ?, email = ?, telefono = ?,
                compania_aseguradora = ?, numero_poliza = ?, endoso = ?, inciso = ?,
                vigencia_inicio = ?, vigencia_fin = ?, forma_pago = ?,
                fecha_vencimiento_pago = ?, tipo_moneda = ?, marca = ?, modelo = ?, tipo_version = ?,
                anio = ?, serie_vin = ?, motor = ?, placas = ?, uso = ?, servicio = ?,
                ultimo_movimiento = ?, prima_total = ?, coberturas_json = ?, comentarios = ?,
                fecha_actualizacion = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (
            datos.get('nombre_completo', ''),
            datos.get('calle', ''),
            datos.get('numero', ''),
            datos.get('codigo_postal', ''),
            datos.get('colonia', ''),
            datos.get('municipio', ''),
            datos.get('estado', ''),
            datos.get('rfc', ''),
            datos.get('email', ''),
            datos.get('telefono', ''),
            datos.get('compania_aseguradora', ''),
            datos.get('numero_poliza', ''),
            datos.get('endoso', ''),
            datos.get('inciso', ''),
            datos.get('vigencia_inicio', ''),
            datos.get('vigencia_fin', ''),
            datos.get('forma_pago', ''),
            datos.get('fecha_vencimiento_pago', ''),
            datos.get('tipo_moneda', 'MXN'),
            datos.get('marca', ''),
            datos.get('modelo', ''),
            datos.get('tipo_version', ''),
            datos.get('anio', ''),
            datos.get('serie_vin', ''),
            datos.get('motor', ''),
            datos.get('placas', ''),
            datos.get('uso', ''),
            datos.get('servicio', ''),
            datos.get('ultimo_movimiento', ''),
            datos.get('prima_total', 0.0),
            datos.get('coberturas_json', ''),
            datos.get('comentarios', ''),
            poliza_id
        ))
        
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def eliminar_poliza(self, poliza_id: int) -> bool:
        """Elimina una póliza de la base de datos."""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM polizas WHERE id = ?', (poliza_id,))
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success
    
    def obtener_poliza(self, poliza_id: int) -> Optional[Dict]:
        """Obtiene una póliza por su ID."""
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM polizas WHERE id = ?', (poliza_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def buscar_polizas(self, termino: str = "") -> List[Dict]:
        """
        Busca pólizas por término de búsqueda.
        Busca en TODOS los campos: datos personales, póliza y vehículo.
        """
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if termino:
            termino_like = f"%{termino}%"
            cursor.execute('''
                SELECT * FROM polizas
                WHERE nombre_completo LIKE ?
                   OR calle LIKE ?
                   OR numero LIKE ?
                   OR codigo_postal LIKE ?
                   OR colonia LIKE ?
                   OR municipio LIKE ?
                   OR estado LIKE ?
                   OR rfc LIKE ?
                   OR email LIKE ?
                   OR telefono LIKE ?
                   OR compania_aseguradora LIKE ?
                   OR numero_poliza LIKE ?
                   OR endoso LIKE ?
                   OR inciso LIKE ?
                   OR marca LIKE ?
                   OR modelo LIKE ?
                   OR tipo_version LIKE ?
                   OR anio LIKE ?
                   OR serie_vin LIKE ?
                   OR motor LIKE ?
                   OR placas LIKE ?
                ORDER BY nombre_completo
            ''', (termino_like, termino_like, termino_like, termino_like, 
                  termino_like, termino_like, termino_like, termino_like,
                  termino_like, termino_like, termino_like, termino_like,
                  termino_like, termino_like, termino_like, termino_like,
                  termino_like, termino_like, termino_like, termino_like, termino_like))
        else:
            cursor.execute('SELECT * FROM polizas ORDER BY nombre_completo')
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def obtener_todas_polizas(self) -> List[Dict]:
        """Obtiene todas las pólizas."""
        return self.buscar_polizas("")
    
    def obtener_alertas_vencimientos(self) -> List[Dict]:
        """
        Obtiene pólizas que están por vencer (<= 15 días)
        tanto en cobertura como en pago.
        """
        polizas = self.obtener_todas_polizas()
        alertas = []
        hoy = datetime.now().date()
        
        # El usuario pidió alertas para 15, 7, 2, etc. (se alertará si es <= 15 días activos)
        rango_interes = range(0, 16)
        
        for poliza in polizas:
            poliza_info = poliza.copy()
            poliza_info['alerta_cobertura'] = None
            poliza_info['alerta_pago'] = None
            
            # Verificar cobertura
            if poliza.get('vigencia_fin'):
                try:
                    fecha_fin = datetime.strptime(poliza['vigencia_fin'], '%d-%m-%Y').date()
                    dias_restantes = (fecha_fin - hoy).days
                    if dias_restantes in rango_interes:
                        poliza_info['alerta_cobertura'] = dias_restantes
                except ValueError:
                    pass
                    
            # Verificar pago
            if poliza.get('fecha_vencimiento_pago'):
                try:
                    fecha_pago = datetime.strptime(poliza['fecha_vencimiento_pago'], '%d-%m-%Y').date()
                    dias_restantes = (fecha_pago - hoy).days
                    if dias_restantes in rango_interes:
                        poliza_info['alerta_pago'] = dias_restantes
                except ValueError:
                    pass
            
            if poliza_info['alerta_cobertura'] is not None or poliza_info['alerta_pago'] is not None:
                alertas.append(poliza_info)
                
        # Ordenar alertas para que los de menor tiempo aparezcan primero
        def get_min_dias(p):
            c1 = p['alerta_cobertura'] if p['alerta_cobertura'] is not None else 999
            c2 = p['alerta_pago'] if p['alerta_pago'] is not None else 999
            return min(c1, c2)
            
        alertas.sort(key=get_min_dias)
        return alertas
    
    def verificar_vencimientos(self, poliza: Dict) -> bool:
        """
        Verifica si una póliza tiene vencimientos próximos (menos de 15 días).
        Retorna True si hay algún vencimiento próximo.
        """
        hoy = datetime.now().date()
        limite = hoy + timedelta(days=15)
        
        # Verificar fecha de vencimiento de pago
        if poliza.get('fecha_vencimiento_pago'):
            try:
                fecha_venc = datetime.strptime(poliza['fecha_vencimiento_pago'], '%d-%m-%Y').date()
                if hoy <= fecha_venc <= limite:
                    return True
            except ValueError:
                pass
        
        # Verificar vigencia fin
        if poliza.get('vigencia_fin'):
            try:
                vigencia_fin = datetime.strptime(poliza['vigencia_fin'], '%d-%m-%Y').date()
                if hoy <= vigencia_fin <= limite:
                    return True
            except ValueError:
                pass
        
        return False
    
    # ============================================================================
    # MÉTODOS DE AUTENTICACIÓN
    # ============================================================================
    
    def verificar_credenciales(self, usuario: str, password: str) -> Optional[Dict]:
        """
        Verifica las credenciales de usuario.
        Retorna los datos del usuario si son correctas, None si no.
        """
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Hash de la contraseña proporcionada
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = ? AND password_hash = ? AND activo = 1",
            (usuario, password_hash)
        )
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return dict(row)
        return None
    
    def generar_password_temporal(self, longitud: int = 12) -> str:
        """Genera una contraseña temporal aleatoria."""
        caracteres = string.ascii_letters + string.digits + "!@#$%&*"
        password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        return password
    
    def enviar_email_password(self, destinatario: str, usuario: str, password: str, 
                               smtp_server: str = "smtp.gmail.com", 
                               smtp_port: int = 587,
                               email_remitente: str = "",
                               email_password: str = "") -> bool:
        """
        Envía un correo electrónico con la contraseña temporal.
        
        Args:
            destinatario: Email del destinatario
            usuario: Usuario creado
            password: Contraseña temporal
            smtp_server: Servidor SMTP
            smtp_port: Puerto SMTP
            email_remitente: Email del remitente
            email_password: Contraseña del email remitente
            
        Returns:
            True si se envió correctamente, False si hubo error
        """
        if not email_remitente or not email_password:
            # Si no hay credenciales, retornar False (no enviar)
            return False
            
        try:
            # Crear mensaje
            mensaje = MIMEMultipart("alternative")
            mensaje["Subject"] = "ASEGURNASA - Contraseña Temporal"
            mensaje["From"] = email_remitente
            mensaje["To"] = destinatario
            
            # Contenido HTML
            html = f"""
            <html>
                <body style="font-family: Arial, sans-serif; padding: 20px; background-color: #f5f5f5;">
                    <div style="max-width: 600px; margin: 0 auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                        <div style="text-align: center; margin-bottom: 30px;">
                            <h1 style="color: #1e3a8a; margin: 0;">🚗 ASEGURNASA</h1>
                            <p style="color: #64748b; margin: 5px 0;">Sistema de Gestión de Pólizas</p>
                        </div>
                        
                        <div style="background-color: #eff6ff; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
                            <h2 style="color: #1e40af; margin-top: 0;">Bienvenido al Sistema</h2>
                            <p style="color: #334155; font-size: 15px; line-height: 1.6;">
                                Se ha creado una cuenta de usuario para acceder al sistema ASEGURNASA.
                                A continuación encontrará sus credenciales de acceso:
                            </p>
                        </div>
                        
                        <div style="background-color: #fef3c7; padding: 20px; border-radius: 8px; border-left: 4px solid #f59e0b; margin-bottom: 20px;">
                            <p style="margin: 0 0 10px 0; color: #92400e; font-weight: bold;">
                                📌 CREDENCIALES DE ACCESO
                            </p>
                            <p style="margin: 5px 0; color: #451a03;">
                                <strong>Usuario:</strong> <span style="font-family: 'Courier New', monospace; background-color: white; padding: 2px 8px; border-radius: 4px;">{usuario}</span>
                            </p>
                            <p style="margin: 5px 0; color: #451a03;">
                                <strong>Contraseña Temporal:</strong> <span style="font-family: 'Courier New', monospace; background-color: white; padding: 2px 8px; border-radius: 4px;">{password}</span>
                            </p>
                        </div>
                        
                        <div style="background-color: #fee2e2; padding: 20px; border-radius: 8px; border-left: 4px solid #dc2626; margin-bottom: 20px;">
                            <p style="margin: 0 0 10px 0; color: #991b1b; font-weight: bold;">
                                ⚠️ IMPORTANTE - SEGURIDAD
                            </p>
                            <ul style="margin: 5px 0; padding-left: 20px; color: #7f1d1d;">
                                <li>Esta es una contraseña temporal generada automáticamente</li>
                                <li>Deberá cambiarla en su primer inicio de sesión</li>
                                <li>No comparta estas credenciales con nadie</li>
                                <li>Si no solicitó estas credenciales, contacte al administrador</li>
                            </ul>
                        </div>
                        
                        <div style="text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e5e7eb;">
                            <p style="color: #94a3b8; font-size: 12px; margin: 0;">
                                Este es un mensaje automático del sistema ASEGURNASA<br>
                                Por favor no responda a este correo
                            </p>
                        </div>
                    </div>
                </body>
            </html>
            """
            
            parte_html = MIMEText(html, "html")
            mensaje.attach(parte_html)
            
            # Enviar email
            with smtplib.SMTP(smtp_server, smtp_port) as servidor:
                servidor.starttls()
                servidor.login(email_remitente, email_password)
                servidor.send_message(mensaje)
            
            return True
            
        except Exception as e:
            print(f"Error al enviar email: {str(e)}")
            return False
    
    def agregar_usuario(self, usuario: str, nombre_completo: str = "", email: str = "",
                        enviar_email: bool = True, smtp_config: Dict = None) -> tuple:
        """
        Agrega un nuevo usuario al sistema con contraseña temporal.
        
        Returns:
            (exito: bool, password_temporal: str, mensaje: str)
        """
        try:
            # Generar contraseña temporal
            password_temporal = self.generar_password_temporal()
            password_hash = hashlib.sha256(password_temporal.encode()).hexdigest()
            
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(
                """INSERT INTO usuarios (usuario, password_hash, nombre_completo, email, 
                   cambiar_password, password_temporal, ultimo_cambio_password) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (usuario, password_hash, nombre_completo, email, 1, 1, datetime.now().isoformat())
            )
            
            conn.commit()
            conn.close()
            
            # Intentar enviar email si se proporcionó
            email_enviado = False
            if enviar_email and email and smtp_config:
                email_enviado = self.enviar_email_password(
                    destinatario=email,
                    usuario=usuario,
                    password=password_temporal,
                    smtp_server=smtp_config.get('servidor', 'smtp.gmail.com'),
                    smtp_port=smtp_config.get('puerto', 587),
                    email_remitente=smtp_config.get('email', ''),
                    email_password=smtp_config.get('password', '')
                )
            
            if email_enviado:
                mensaje = f"Usuario creado exitosamente. Se envió email a {email}"
            else:
                mensaje = f"Usuario creado. Contraseña temporal: {password_temporal}"
            
            return (True, password_temporal, mensaje)
            
        except sqlite3.IntegrityError:
            return (False, "", "El usuario ya existe en el sistema")
        except Exception as e:
            return (False, "", f"Error al crear usuario: {str(e)}")
    
    def cambiar_password(self, usuario: str, password_actual: str, password_nuevo: str) -> tuple:
        """
        Cambia la contraseña de un usuario.
        
        Returns:
            (exito: bool, mensaje: str)
        """
        # Verificar contraseña actual
        if not self.verificar_credenciales(usuario, password_actual):
            return (False, "La contraseña actual es incorrecta")
        
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            password_hash = hashlib.sha256(password_nuevo.encode()).hexdigest()
            cursor.execute(
                """UPDATE usuarios 
                   SET password_hash = ?, cambiar_password = 0, password_temporal = 0,
                       ultimo_cambio_password = ?
                   WHERE usuario = ?""",
                (password_hash, datetime.now().isoformat(), usuario)
            )
            
            conn.commit()
            conn.close()
            return (True, "Contraseña cambiada exitosamente")
            
        except Exception as e:
            return (False, f"Error al cambiar contraseña: {str(e)}")
    
    def listar_usuarios(self) -> List[Dict]:
        """Obtiene la lista de todos los usuarios."""
        conn = self.get_connection()
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, usuario, nombre_completo, email, activo, 
                   cambiar_password, password_temporal, fecha_creacion
            FROM usuarios 
            ORDER BY usuario
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def activar_desactivar_usuario(self, usuario: str, activo: bool) -> bool:
        """Activa o desactiva un usuario."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(
                "UPDATE usuarios SET activo = ? WHERE usuario = ?",
                (1 if activo else 0, usuario)
            )
            
            conn.commit()
            conn.close()
            return True
        except Exception:
            return False
