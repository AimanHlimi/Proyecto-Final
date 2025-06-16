## 📖 ¿Que es CarNow?

### CarNow es una pagina web que se dedica a la compra-venta de vehiculos

### tanto importados, como de segunda mano, nuevos, en el que los usuarios o

### empresas pueden publicar sus vehiculos (tanto coches como motos, aviones,

### barcos, etc) para venderlo y que otros usuarios puedan comprar lo que mas le

### gusten o necesiten

## 🚗 ¿Qué puedes hacer con CarNow?

### ✅ Crear tu cuenta

### Antes de usar todas las funciones, debes registrarte. Solo necesitas llenar un

### formulario con tus datos como nombre, email, teléfono, y elegir un usuario y

### contraseña.

### ✅ Iniciar sesión

### Una vez registrado, puedes iniciar sesión con tu usuario y contraseña para

### acceder a tu perfil, publicar coches o comprarlos.

### ✅ Publicar un coche en venta

### Si tienes un coche que quieres vender:

### 1. Accede a la sección "Publicar".

### 2. Rellena los datos del coche (marca, modelo, año, precio, tipo,

### transmisión, etc.).

### 3. Sube una imagen del coche.

### 4. Haz clic en "Publicar" y ¡tu coche ya estará visible para otros usuarios!

### ✅ Buscar y filtrar coches

### Desde la página principal puedes:


### ● Ver todos los coches disponibles.

### ● Usar filtros para buscar por marca, tipo, año, precio, provincia y más.

### ● Ver detalles completos de cada coche con solo un clic.

### ✅ Comprar un coche

### ¿Te interesa un coche? Haz clic en "Comprar". El sistema:

### ● Te guarda como comprador de ese coche.

### ● Cambia el estado del coche a "Vendido" , para que otros no lo

### compren.

### ● Guarda al vendedor original como quien realizó la venta.

### ✅ Acceder a tu perfil

### En tu perfil puedes:

### ● Ver todos los coches que tú has puesto en venta.

### ● Editar los datos de tus coches si necesitas cambiar precio, imagen o

### descripción.

### ● Ver el estado de tus vehículos.

## 🔐 Seguridad y privacidad

### ● Solo tú puedes ver o editar los coches que has publicado.

### ● La plataforma guarda la fecha de registro y no muestra tus datos

### personales públicamente.

### ● La contraseña está protegida y nadie más puede verla.


## 🏠 Inicio

Página principal de la aplicación:
● Muestra todos los coches **en venta**.
● Tiene una barra lateral con filtros avanzados: marca, modelo, tipo, año, km, precio,
etc.
● Cada coche se presenta como una tarjeta con imagen, información y botón “Ver”.
● Al hacer clic en “Ver”, se abre la página de detalle.
Al darle a var nos aparecera lo siguiente:

## 📄 detalle.html

Página individual de cada coche:
● Muestra la imagen grande del coche.
● Todos los datos técnicos y de ubicación.
● Información de contacto del vendedor.
● Botón “Comprar”:


○ Inserta una fila en compras para el comprador.
○ Inserta una fila en ventas para el vendedor.
○ Cambia el estado del coche a "VENDIDO" (ya no aparece en el inicio).


## 🔐 login.html

Formulario sencillo de acceso:
● Campos: usuario, contraseña
● Acción: valida los datos y permite iniciar sesión.
● Estilo centrado con caja blanca, sombra y botón oscuro.
● Enlace a la página de registro si el usuario no tiene cuenta.


## 📝 registro.html

Formulario de creación de cuenta:
● Recoge DNI, nombre, apellido, usuario, email, teléfono, contraseña, y
dirección.
● Se conecta a la base de datos e inserta al nuevo usuario si los datos son válidos.
● Previene duplicados de DNI, email, usuario y teléfono.


## 🚘 Publicar

Formulario para publicar un nuevo vehículo:
● Campos: matrícula, marca, modelo, año, potencia, tipo, combustible,
transmisión, provincia, precio, kilometraje, imagen, descripción.
● Al enviar, guarda los datos y sube la imagen al servidor (/static/uploads).
● Agrega el coche a la base de datos con estado "EN VENTA".


## 👤 perfil.html

Panel de usuario:
● Muestra los coches que el usuario ha publicado.
● Botón “Editar” para modificar los datos del coche.
● Opción para eliminar si se implementa.
● El coche se puede editar a través del formulario editar_vehiculo.html.
● Boton para ver los coches vendidos
● Boton para ver coches comprados
● Boton para poder editar tus datos
