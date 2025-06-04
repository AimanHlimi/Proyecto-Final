-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS carnow;
USE carnow;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS  usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    dni VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    usuario VARCHAR(20) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) UNIQUE,
    direccion TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de vehículos (versión con imagen binaria)
CREATE TABLE IF NOT EXISTS vehiculos (
    matricula VARCHAR(7) PRIMARY KEY NOT NULL,
    id_vendedor INT,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    potencia INT NOT NULL,
    anio INT NOT NULL,
    transmision VARCHAR(20) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    combustible VARCHAR(50) NOT NULL,
    provincia VARCHAR(50) NOT NULL,
    kilometraje INT NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT,
    imagen TEXT NOT NULL,
    estado VARCHAR(8) DEFAULT 'EN VENTA',
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_vendedor) REFERENCES usuarios(id_usuario)
);

-- Tabla de compras
CREATE TABLE IF NOT EXISTS  compras (
    id_compra INT PRIMARY KEY AUTO_INCREMENT,
    id_comprador INT,
    id_vehiculo VARCHAR(7),
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    precio_final DECIMAL(10, 2),
    FOREIGN KEY (id_comprador) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(matricula)
);

-- Tabla de ventas
CREATE TABLE IF NOT EXISTS  ventas (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_vendedor INT,
    id_vehiculo VARCHAR(7),
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    precio_venta DECIMAL(10, 2),
    FOREIGN KEY (id_vendedor) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(matricula)
);

INSERT INTO usuarios (dni, nombre, apellido, email, usuario, contrasena, telefono, direccion)
VALUES
('12345678A', 'Aiman', 'Hlimi', 'aiman@gmail.com', 'aiman', '1234', '600000001', 'Calle Falsa 123, Madrid'),
('23456789B', 'Lucía', 'Gómez', 'lucia.gomez@example.com', 'luciag', '1234', '600000002', 'Av. del Sol 45, Valencia'),
('34567890C', 'Pedro', 'López', 'pedro.lopez@example.com', 'pedrol', '1234', '600000003', 'C/ Mayor 22, Sevilla'),
('45678901D', 'María', 'Ruiz', 'maria.ruiz@example.com', 'mariar', '1234', '600000004', 'Paseo del Río 99, Zaragoza'),
('56789012E', 'Ana', 'Fernández', 'ana.fernandez@example.com', 'anaf', '1234', '600000005', 'Calle Luna 7, Bilbao');
