# 🧾 ¿Qué es CarNow?

**CarNow** es una plataforma web desarrollada para facilitar la **compra y venta de vehículos
entre particulares** , ofreciendo una interfaz intuitiva, segura y adaptada al usuario final. Es
ideal tanto para quienes desean vender su coche de forma rápida como para quienes están
buscando su próximo vehículo desde la comodidad de su casa.

# 🎯 Objetivo principal

El objetivo de CarNow es permitir que cualquier usuario pueda:
● **Publicar un coche en venta** fácilmente, añadiendo sus datos, imagen, precio, y
características.
● **Explorar coches disponibles** , usando filtros avanzados como marca, tipo, precio,
año, transmisión, etc.
● **Ver información detallada** de cada vehículo y contactar directamente con el
vendedor.
● **Realizar una compra** que queda registrada en el sistema (simulada, sin pago en
línea).
● **Gestionar sus publicaciones** desde su perfil (editar, eliminar, ver estado).

# 🧩 Funcionalidades principales

## ✅ Registro e inicio de sesión

```
● Registro de usuarios con campos como nombre, apellido, DNI, teléfono, etc.
● Inicio de sesión seguro con verificación de credenciales.
● Gestión de sesión para mostrar contenido personalizado.
```
## ✅ Publicación de vehículos

```
● Los usuarios registrados pueden subir un coche a la venta.
```

```
● El formulario incluye: matrícula, marca, modelo, año, potencia, tipo, transmisión,
combustible, precio, descripción e imagen.
● Los vehículos se almacenan con estado "EN VENTA" por defecto.
```
## ✅ Visualización y filtrado

```
● Los coches se muestran con tarjetas visuales.
● Filtros por marca, modelo, año, tipo, combustible, transmisión, provincia, y precio.
● Detalles completos disponibles al hacer clic en un coche.
```
## ✅ Compra y distribución

```
● Al pulsar "Comprar", el coche:
○ Cambia su estado a "VENDIDO".
○ Se registra en la tabla compras para el comprador.
○ Se registra en la tabla ventas para el vendedor.
```
## ✅ Gestión del perfil

```
● Cada usuario puede:
○ Ver los coches que ha publicado.
○ Editar la información de sus vehículos.
○ (Opcional) Eliminar vehículos.
```
# 🛠 Estructura técnica

```
● Frontend : HTML, CSS puro, Bootstrap 5 para estilos rápidos y responsive.
● Backend : Python con Flask.
```

```
● Base de datos : MySQL, con tablas bien estructuradas (usuarios, vehiculos,
compras, ventas).
● Seguridad : Contraseñas encriptadas con werkzeug.security.
```
# 🧠 Público objetivo

```
● Usuarios que quieren vender su coche de segunda mano sin intermediarios.
● Personas que buscan vehículos usados , con la posibilidad de contactar
directamente con el dueño.
```
# 🌐 Potencial futuro

CarNow puede evolucionar fácilmente con nuevas funcionalidades como:
● Subida de múltiples imágenes por vehículo (carrusel).
● Chat en tiempo real entre comprador y vendedor.
● Pago seguro dentro de la plataforma.
● Verificación de usuarios o vehículos (mediante documentación).

# 📌 Conclusión

**CarNow** es un proyecto web funcional, claro y escalable que resuelve un problema real:
**facilitar el proceso de compra y venta de coches** entre usuarios sin complicaciones
técnicas ni intermediarios.


# 💾 Base de datos

Compuesta por:
● usuarios: almacena la información del usuario.
● vehiculos: coches en venta (con campo estado para control de disponibilidad).


● compras: historial de coches comprados por cada usuario.
● ventas: historial de coches vendidos por cada usuario.


# 🔐 login.html

El login está formado por un sencillo formulario html donde se recoge el nombre de usuario
y la contraseña del usuario que quiera tanto vender como comprar un vehículo.

## 🔸 @app.route('/login', methods=['GET', 'POST'])

En el app.py esta de la siguiente forma:
Tenemos una función llamada login() el la que podemos ver que recogemos los valores de
los campos usuario y contraseña de inicio de sesion. Una vez recogidos y guardados en las


variables conectamos con mi base de datos y ejecutamos una consulta en el que
seleccionamos todo de la tabla usuario donde el usuario y la contraseña coincida con la que
hemos rellenado los campos de inicio de sesion. Una vez hecho guardamos tanto el usuario
como su dni para mantener la sesion iniciada y nos dirigira a la funcion mostrar_vehiculos
que seria la pagina principal de la aplicacion web pero ya con el inicio de sesion
completado.

# 📝 registro.html

Es un formulario html sencillo donde el usuario tendra que rellenar los campos con sus
datos.


Al darle a Registrarse nos iremos a la funcion app.py:
Esta funcion es bastante sencilla ya que primero recogemos los datos del formulario,
despues hacemos un select para ver si el usuario ya existe y si no existe lo que hace es
insertarlo en la base de datos y dirigirnos a la pagina de inicio de sesion.

# 🚘 publicar.html

En este html lo que se tiene es un formulario para rellenar los campos con los datos del
vehiculo que queremos vender asi como su matricula que seria lo principal, la marca y
modelo, unos select de tipo para saber el tipo de vehiculo vendemos si es un suv un sedan,
etc, otro como el combustible y la transmision



En el app.py tenemos lo siguiente:
Lo primero es una comprobacion para ver si se ha iniciado sesion y si no es asi dirigirnos a
la pagina de inicio de sesion.


Una vez comprobado el inicio de sesion hacemos lo mismo que en los anteriores.
Guardamos los valores del formularios en sus variable correspondientes y hacemos un
insert a la tabla de vehiculos.
Para la imagen lo que hacemos es almacenarla en la carpeta static.


# 🏠 inicio.html

Está compuesto por una barra de navegacion donde tendremos un logo un enlace para
volver al inicio, para ir a la parte del formulario donde publicaremos nuestro vehiculo y para
ir a nuestro perfil.


Tambien tendremos un aside donde tendremos un formulario para poder filtrar por las
caracteristicas del vehiculo que queramos.


En ella podemos ver varios campos en el que usarmos request.arg.get que sirve para
obtener parametros que vienen de del formulario.
Tambien tenemos el main que es donde nos mostrara todos los vehiculos que estan a la
venta:
Lo que usamos en una carta de bootstrap en la que recogemos la imagen que se guardan
en una carpeta llamada static, la marca y el modelo del vehiculo, la informacion como el año
los kilometros , el tipo de vehiculo y la transmision, la provincia en la que se encuentra e
vehiculo y un boton que nos manda a la funcion detalle de nuestro app.py en la que
creamos una variable llamada matricula.

## 🔸 @app.route('/')

En la funcion mostrar_vehiculos podremos ver varias cosas.
La primera son lor argumentos que le hemos pasado por el filtro de nuestro inicio en la que
usamos la misma funcion request.arg.get para pedir datos del servidor
Luego tenemos un query para realizar las consultas sql para que nos muestre todos los
vehiculos,



## 🔧 1. Consulta base con WHERE 1=

python
CopiarEditar
query = "SELECT * FROM vehiculos WHERE 1=1"
params = []
● WHERE 1=1 sirve como base para agregar condiciones fácilmente con AND después.
● params es una lista que almacenará los valores reales que se insertarán en la
consulta de forma segura ( **evitando inyección SQL** ).

## 🧩 2. Agrega filtros si el usuario los proporciona

Cada condición solo se agrega si la variable correspondiente (marca, modelo, etc.) tiene
un valor. Por ejemplo:
python
CopiarEditar
if marca:
query += " AND marca LIKE %s"
params.append(f"%{marca}%")
● Agrega AND marca LIKE %s a la consulta.
● Usa %{marca}% para búsqueda parcial (como LIKE '%Toyota%').
● El %s es un **placeholder seguro** : se reemplaza por el valor real **en el método
cursor.execute(query, params)** , evitando inyección SQL.
Esto mismo se repite para:


```
● modelo → búsqueda parcial con LIKE.
● anio_min, anio_max → rangos de años.
● km_max → máximo kilometraje.
● tipo, combustible, transmision → igualdad exacta.
● provincia → búsqueda parcial.
● precio_max → tope de precio.
```
## 🟩 3. Condición fija + ordenamiento

python
CopiarEditar
query += " AND estado = 'EN VENTA'"
query += " ORDER BY fecha_publicacion DESC"
● Solo muestra los vehículos con estado "EN VENTA".
● Ordena los resultados por fecha de publicación más reciente primero.

## 💾 4. Ejecuta la consulta y devuelve resultados

python
CopiarEditar
cursor.execute(query, params)
vehiculos = cursor.fetchall()
cursor.close()


conn.close()
● Ejecuta la consulta construida con los parámetros.
● Recupera los resultados.
● Cierra el cursor y la conexión.
● Devuelve los datos a la plantilla inicio.html.

# 📄 detalle.html


## 🚗 Barra de navegación (<nav>)

html
CopiarEditar
<nav>
<img src="{{ url_for('static', filename='logo.png') }}"
alt="CarNow">
<div class="nav-links">


<a href="/">Inicio</a>
<a href="/publicar">Publicar</a>
<a href="/perfil">Perfil</a>
</div>
</nav>
● {{ url_for('static', filename='logo.png') }} genera la URL del
archivo logo.png ubicado en la carpeta /static.
● Esto asegura que Flask pueda servir la imagen correctamente.
● Las etiquetas <a> son enlaces a las secciones principales del sitio.

## 🖼 Imagen del vehículo

html
CopiarEditar
<img src="{{ url_for('static', filename=vehiculo.imagen) }}"
alt="Imagen vehículo" class="car-image">
● Muestra la imagen del vehículo almacenada en el campo vehiculo.imagen.
● Se asume que la imagen está guardada en la carpeta static/.

## 📝 Información del vehículo

html
CopiarEditar
<h2>{{ vehiculo.marca }} {{ vehiculo.modelo }}</h2>


<h4>{{ "%.2f"|format(vehiculo.precio) }} €</h4>
<p>{{ vehiculo.descripcion }}</p>
● Muestra marca, modelo y descripción.
● El precio se formatea con **2 decimales** gracias a |format.

## 📊 Cuadro con detalles técnicos

html
CopiarEditar
<div class="info-grid">
<div class="info-item"><strong>Año:</strong> {{ vehiculo.anio
}}</div>
...
</div>
● Muestra detalles clave como:
○ Año
○ Kilometraje
○ Potencia (CV)
○ Combustible
○ Transmisión
○ Tipo de coche
○ Provincia
○ Matrícula


## 📞 Información de contacto

html
CopiarEditar
<div class="contact-info">
<h5>Contacto del vendedor</h5>
<p><strong>Nombre:</strong> {{ vehiculo.vendedor_nombre }}</p>
<p><strong>Email:</strong> {{ vehiculo.email }}</p>
<p><strong>Teléfono:</strong> {{ vehiculo.telefono }}</p>
</div>
● Datos del vendedor para contactar directamente.
● Todos estos campos se asumen que están en el objeto vehiculo.

## 🛒 Formulario de compra

html
CopiarEditar
<form method="post" action="{{ url_for('comprar_vehiculo') }}">
<input type="hidden" name="matricula" value="{{ vehiculo.matricula
}}">
<button type="submit" class="btn-orange">Comprar</button>
</form>
● Al pulsar el botón **“Comprar”** , se envía un formulario por **POST** a la ruta
/comprar_vehiculo.


```
● La matrícula se pasa como campo oculto, probablemente para identificar qué coche
está comprando el usuario.
```
## 🔸 @app.route('/vehiculo/<matricula>')

## 🧭 Ruta de Flask

python
CopiarEditar
@app.route('/vehiculo/<matricula>')
def detalle(matricula):
Define una ruta como /vehiculo/<matricula>, por ejemplo:
bash
CopiarEditar
/vehiculo/ABC123
●
● El valor <matricula> se extrae de la URL y se pasa como argumento a la función
detalle(matricula).

## 🔍 Consulta SQL para obtener el vehículo

python
CopiarEditar
cursor.execute("""
SELECT v.*, u.nombre AS vendedor_nombre, u.telefono, u.email
FROM vehiculos v
JOIN usuarios u ON v.id_vendedor = u.id_usuario
WHERE v.matricula = %s
""", (matricula,))
vehiculo = cursor.fetchone()


```
● Se hace un join entre vehiculos y usuarios para obtener tanto los datos del
coche como del vendedor.
● El WHERE v.matricula = %s filtra por la matrícula recibida en la URL.
● Se usa una tupla (matricula,) para evitar inyección SQL.
● cursor.fetchone() devuelve un solo resultado (el vehículo con esa matrícula), o
None si no existe.
```
## 🖼 Renderizado de la plantilla

python
CopiarEditar
if vehiculo:
return render_template('detalle.html', vehiculo=vehiculo)
else:
return "Vehículo no encontrado", 404
● Si se encontró el vehículo:
○ Se renderiza la plantilla detalle.html, pasando el diccionario vehiculo.
● Si no existe:
○ Se devuelve un mensaje de error "Vehículo no encontrado" y código
**HTTP 404**.


