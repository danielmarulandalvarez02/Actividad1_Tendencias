
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10,2) NOT NULL
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id),
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL
);


INSERT INTO clientes (nombre, email) VALUES
('Juan Pérez', 'juan@gmail.com'),
('María Gómez', 'maria@gmail.com'),
('Carlos López', 'carlos@gmail.com'),
('Ana Torres', 'ana@gmail.com'),
('Luis Martínez', 'luis@gmail.com');

INSERT INTO productos (nombre, precio) VALUES
('Laptop', 2500000),
('Mouse', 25000),
('Teclado', 80000),
('Monitor', 130000),
('Audífonos', 40000);

INSERT INTO pedidos (cliente_id, producto_id, cantidad) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 1),
(4, 4, 1),
(5, 5, 3);