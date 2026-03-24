🛒 Sistema de Ventas (Dockerizado)

Descripción
Este proyecto corresponde al desarrollo de un sistema de ventas básico utilizando una arquitectura de tres capas, completamente dockerizada. El sistema permite gestionar clientes y productos mediante operaciones CRUD (crear, listar, actualizar y eliminar).Docker permite ejecutar cada componente del sistema en contenedores independientes, facilitando la portabilidad, el despliegue y la integración entre servicios como backend, frontend y base de datos.

Tecnologías utilizadas:
Frontend: HTML + Nginx
Backend: Flask (Python)
Base de datos: PostgreSQL
Administración BD: pgAdmin
Contenedores: Docker + Docker Compose

Requisitos:
Para ejecutar el proyecto se necesita:
Docker instalado
Docker Compose instalado

Instrucciones de uso:
Descargar o descomprimir el proyecto. 
Abrir una terminal en la carpeta raíz del proyecto.
Ejecutar el siguiente comando: docker compose up -d --build
Verificar que los contenedores estén corriendo: docker compose ps

Acceder a los servicios desde el navegador:
Frontend: http://localhost:3000
API: http://localhost:5000/productos
pgAdmin: http://localhost:8080
Evidencias de funcionamiento.

1. Contenedores en ejecución.
Se ejecuta el comando: docker compose ps




 3. API funcionando.
Acceso a:localhost:5000/productos


 4. Frontend funcionando
Acceso a: http://localhost:3000/  .
