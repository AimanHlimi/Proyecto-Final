from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'aiman'

# Carpeta donde se guardarán las imágenes subidas
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Conexión con la base de datos MySQL
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'rootpassword'),
        database=os.getenv('MYSQL_DATABASE', 'carnow')
    )
    return connection

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s;', (usuario, contrasena))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        if usuario:
            session['usuario'] = usuario['usuario']
            session['dni'] = usuario['dni']
            return redirect(url_for('mostrar_vehiculos'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return render_template('inicioSesion.html')

    return render_template('inicioSesion.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('rol', None)
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('login')) 

@app.route('/')
def mostrar_vehiculos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # --- Filtros desde el formulario --- Se usa el request.args.get para el metodo GET para pedir datos del servidor
    marca = request.args.get('marca')
    modelo = request.args.get('modelo')
    anio_min = request.args.get('anio_min')
    anio_max = request.args.get('anio_max')
    km_max = request.args.get('km_max')
    tipo = request.args.get('tipo')
    combustible = request.args.get('combustible')
    transmision = request.args.get('transmision')
    provincia = request.args.get('provincia')
    precio_max = request.args.get('precio_max')

    # --- Consulta SQL dinámica ---
    query = "SELECT * FROM vehiculos WHERE 1=1"
    params = []

    if marca:
        query += " AND marca LIKE %s"
        params.append(f"%{marca}%")
    if modelo:
        query += " AND modelo LIKE %s"
        params.append(f"%{modelo}%")
    if anio_min:
        query += " AND anio >= %s"
        params.append(anio_min)
    if anio_max:
        query += " AND anio <= %s"
        params.append(anio_max)
    if km_max:
        query += " AND kilometraje <= %s"
        params.append(km_max)
    if tipo:
        query += " AND tipo = %s"
        params.append(tipo)
    if combustible:
        query += " AND combustible = %s"
        params.append(combustible)
    if transmision:
        query += " AND transmision = %s"
        params.append(transmision)
    if provincia:
        query += " AND provincia LIKE %s"
        params.append(f"%{provincia}%")
    if precio_max:
        query += " AND precio <= %s"
        params.append(precio_max)

    # Mostrar solo vehículos disponibles en venta
    query += " AND estado = 'EN VENTA'"
    query += " ORDER BY fecha_publicacion DESC"

    cursor.execute(query, params)
    vehiculos = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('inicio.html', vehiculos=vehiculos)


@app.route('/publicar', methods=['GET', 'POST'])
def publicar_vehiculo():
    if request.method == 'POST':
        if 'dni' not in session:
            flash('Debes iniciar sesión para publicar un vehículo.', 'warning')
            return redirect(url_for('login'))

        dni = session['dni']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT id_usuario FROM usuarios WHERE dni = %s', (dni,))
        usuario = cursor.fetchone()

        if not usuario:
            flash('Usuario no encontrado.', 'danger')
            return redirect(url_for('login'))

        id_vendedor = usuario['id_usuario']

        # Datos del formulario
        matricula = request.form['matricula']
        marca = request.form['marca']
        modelo = request.form['modelo']
        potencia = request.form['potencia']
        anio = request.form['anio']
        transmision = request.form['transmision']
        tipo = request.form['tipo']
        combustible = request.form['combustible']
        provincia = request.form['provincia']
        kilometraje = request.form['kilometraje']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        imagen = request.files['imagen']

        # Guardar imagen en static/uploads
        if imagen:
            filename = secure_filename(imagen.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            imagen.save(image_path)
            ruta_imagen = f'uploads/{filename}'  # Ruta relativa desde /static/
        else:
            ruta_imagen = None

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO vehiculos (
                matricula, id_vendedor, marca, modelo, potencia, anio, transmision,
                tipo, combustible, provincia, kilometraje, precio, descripcion, imagen
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            matricula, id_vendedor, marca, modelo, potencia, anio, transmision,
            tipo, combustible, provincia, kilometraje, precio, descripcion, ruta_imagen
        ))

        conn.commit()
        cursor.close()
        conn.close()

        flash('Vehículo publicado correctamente.', 'success')
        return redirect(url_for('mostrar_vehiculos'))

    return render_template('publicar.html')



@app.route('/perfil', methods=['GET'])
def perfil():
    if 'dni' not in session:
        flash('Debes iniciar sesión para acceder al perfil.', 'warning')
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener datos del usuario
    cursor.execute("SELECT * FROM usuarios WHERE dni = %s", (session['dni'],))
    usuario = cursor.fetchone()
    id_usuario = usuario['id_usuario']

    # Coches publicados (vehículos de este usuario que no están en ventas)
    cursor.execute("""
        SELECT v.* FROM vehiculos v
        LEFT JOIN ventas vt ON v.matricula = vt.id_vehiculo
        WHERE v.id_vendedor = %s AND vt.id_vehiculo IS NULL
    """, (id_usuario,))
    coches_publicados = cursor.fetchall()

    # Coches vendidos (relación con la tabla ventas)
    cursor.execute("""
        SELECT v.*, vt.fecha_venta, vt.precio_venta FROM vehiculos v
        JOIN ventas vt ON v.matricula = vt.id_vehiculo
        WHERE vt.id_vendedor = %s
    """, (id_usuario,))
    coches_vendidos = cursor.fetchall()

    # Coches comprados (relación con la tabla compras)
    cursor.execute("""
        SELECT v.*, c.fecha_compra, c.precio_final FROM vehiculos v
        JOIN compras c ON v.matricula = c.id_vehiculo
        WHERE c.id_comprador = %s
    """, (id_usuario,))
    coches_comprados = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("perfil.html",
                           usuario=usuario,
                           coches_usuario=coches_publicados,
                           coches_vendidos=coches_vendidos,
                           coches_comprados=coches_comprados)


@app.route('/actualizar_perfil', methods=['POST'])
def actualizar_perfil():
    if 'dni' not in session:
        flash('No estás autenticado.', 'danger')
        return redirect(url_for('login'))

    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    direccion = request.form['direccion']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE usuarios 
        SET nombre = %s, apellido = %s, email = %s, telefono = %s, direccion = %s 
        WHERE dni = %s
    """, (nombre, apellido, email, telefono, direccion, session['dni']))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Datos actualizados correctamente.', 'success')
    return redirect(url_for('perfil'))


@app.route('/vehiculo/<matricula>')
def detalle(matricula):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener todos los datos del vehículo por matrícula
    cursor.execute("SELECT v.*, u.nombre AS vendedor_nombre, u.telefono, u.email FROM vehiculos v JOIN usuarios u ON v.id_vendedor = u.id_usuario WHERE v.matricula = %s", (matricula,))
    vehiculo = cursor.fetchone()

    cursor.close()
    conn.close()

    if vehiculo:
        return render_template('detalle.html', vehiculo=vehiculo)
    else:
        return "Vehículo no encontrado", 404


@app.route('/editar/<matricula>', methods=['GET', 'POST'])
def editar_vehiculo(matricula):
    if 'dni' not in session:
        flash('Debes iniciar sesión para editar un vehículo.', 'warning')
        return redirect(url_for('login'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener ID del usuario
    cursor.execute("SELECT id_usuario FROM usuarios WHERE dni = %s", (session['dni'],))
    usuario = cursor.fetchone()

    # Verificar que el vehículo pertenece al usuario
    cursor.execute("SELECT * FROM vehiculos WHERE matricula = %s AND id_vendedor = %s", (matricula, usuario['id_usuario']))
    vehiculo = cursor.fetchone()

    if not vehiculo:
        flash('No tienes permiso para editar este vehículo.', 'danger')
        return redirect(url_for('mostrar_vehiculos'))

    if request.method == 'POST':
        matricula = request.form['matricula']
        
        cursor.execute("SELECT * FROM vehiculos WHERE matricula = %s", (matricula,))
        vehiculo = cursor.fetchone()

    cursor.close()
    conn.close()
    return render_template('editar.html', vehiculo=vehiculo)

@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar_vehiculo():
    if request.method:
        matricula = request.form['matricula']
        marca = request.form['marca']
        modelo = request.form['modelo']
        potencia = request.form['potencia']
        anio = request.form['anio']
        transmision = request.form['transmision']
        tipo = request.form['tipo']
        combustible = request.form['combustible']
        provincia = request.form['provincia']
        kilometraje = request.form['kilometraje']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
            
            
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''UPDATE vehiculos
            SET matricula = %s, marca = %s, modelo = %s, potencia = %s, anio = %s, 
            transmision = %s, tipo = %s, combustible = %s, provincia = %s, kilometraje = %s, precio = %s, 
            descripcion = %s
            WHERE matricula = %s
            ''', (matricula, marca, modelo, potencia, anio, transmision, tipo, combustible, 
                  provincia, kilometraje, precio, descripcion, matricula))

        conn.commit()
        cursor.close()
        conn.close()

        flash('Datos actualizados correctamente.', 'success')
        return redirect(url_for('perfil'))
    
@app.route('/comprar', methods=['POST'])
def comprar_vehiculo():
    if 'dni' not in session:
        flash('Debes iniciar sesión para comprar.', 'warning')
        return redirect(url_for('login'))

    matricula = request.form['matricula']

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener ID del comprador
    cursor.execute("SELECT id_usuario FROM usuarios WHERE dni = %s", (session['dni'],))
    comprador = cursor.fetchone()

    # Obtener datos del vehículo
    cursor.execute("SELECT * FROM vehiculos WHERE matricula = %s", (matricula,))
    vehiculo = cursor.fetchone()

    if not vehiculo:
        flash('Vehículo no encontrado.', 'danger')
        return redirect(url_for('mostrar_vehiculos'))

    # Insertar en compras
    cursor.execute("""
        INSERT INTO compras (id_comprador, id_vehiculo, precio_final)
        VALUES (%s, %s, %s)
    """, (comprador['id_usuario'], matricula, vehiculo['precio']))

    # Insertar en ventas
    cursor.execute("""
        INSERT INTO ventas (id_vendedor, id_vehiculo, precio_venta)
        VALUES (%s, %s, %s)
    """, (vehiculo['id_vendedor'], matricula, vehiculo['precio']))

    # (Opcional) Marcar el coche como vendido
    cursor.execute("UPDATE vehiculos SET estado = 'VENDIDO' WHERE matricula = %s", (matricula,))

    conn.commit()
    cursor.close()
    conn.close()

    flash('¡Has comprado el vehículo con éxito!', 'success')
    return redirect(url_for('perfil'))


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        telefono = request.form['telefono']
        direccion = request.form['direccion']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Comprobar si el usuario, email, dni o teléfono ya existen
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s OR email = %s OR dni = %s OR telefono = %s",
                       (usuario, email, dni, telefono))
        existente = cursor.fetchone()
        if existente:
            flash("Ya existe un usuario con ese DNI, email, teléfono o nombre de usuario.")
            return redirect(url_for('registro'))

        # Insertar nuevo usuario
        cursor.execute("""
            INSERT INTO usuarios (dni, nombre, apellido, email, usuario, contrasena, telefono, direccion)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (dni, nombre, apellido, email, usuario, contrasena, telefono, direccion))

        conn.commit()
        cursor.close()
        conn.close()

        flash('Registro exitoso. Ya puedes iniciar sesión.')
        return redirect(url_for('login'))

    return render_template('registrarse.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
