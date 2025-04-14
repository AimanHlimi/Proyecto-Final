-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS carnow;
USE carnow;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de vehículos
CREATE TABLE vehiculos (
    id_vehiculo INT PRIMARY KEY AUTO_INCREMENT,
    id_vendedor INT,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    año INT,
    tipo VARCHAR(50),
    kilometraje INT,
    precio DECIMAL(10, 2),
    descripcion TEXT,
    imagen_url TEXT,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('disponible', 'vendido') DEFAULT 'disponible',
    FOREIGN KEY (id_vendedor) REFERENCES usuarios(id_usuario)
);

-- Tabla de compras
CREATE TABLE compras (
    id_compra INT PRIMARY KEY AUTO_INCREMENT,
    id_comprador INT,
    id_vehiculo INT,
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    precio_final DECIMAL(10, 2),
    FOREIGN KEY (id_comprador) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
);

-- Tabla de ventas
CREATE TABLE ventas (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_vendedor INT,
    id_vehiculo INT,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    precio_venta DECIMAL(10, 2),
    FOREIGN KEY (id_vendedor) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
);
