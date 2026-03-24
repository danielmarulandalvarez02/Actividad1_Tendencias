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

<img width="1600" height="105" alt="1" src="https://github.com/user-attachments/assets/52e7a081-8842-4641-9561-5344fca8d3fa" />

2. API funcionando.
Acceso a:localhost:5000/productos
<img width="368" height="795" alt="2" src="https://github.com/user-attachments/assets/b8d203f1-af43-4f68-b1fc-ebd195a1d072" />

3. Frontend funcionando
Acceso a: http://localhost:3000/
<img width="566" height="170" alt="Captura de pantalla 2026-03-24 103606" src="https://github.com/user-attachments/assets/949c0b0a-4b3d-48b9-87ba-b962b274e8ba" />

4. pgAdmin conectado a la base de datos
Se accede a: http://localhost:8080

Iniciar sesión con las credenciales definidas en el .env
Conectarse al servidor PostgreSQL, con el host, usuario y contraseña.
Finalmente, se accede a:
Databases → (ventas_db) → Schemas → public → Tables, donde se visualizan las tablas creadas
<img width="1423" height="826" alt="5" src="https://github.com/user-attachments/assets/423d43cf-86dd-41c9-9bad-42b00b2a3f4a" />

Pruebas realizadas.
Durante el desarrollo se validaron las siguientes funcionalidades:
✔ Creación de productos
✔ Edición de productos
✔ Eliminación de productos
✔ Listado de productos
El sistema responde correctamente a todas las operaciones realizadas desde el frontend.
 Autores:
Daniel Alejandro Marulanda 
Maria Fernanda Narvaez

Conclusión
Se logró implementar un sistema de ventas funcional utilizando una arquitectura de tres capas y contenedores Docker; esta permitió integrar de forma eficiente el frontend, backend y la base de datos, facilitando el despliegue del sistema en cualquier entorno. Además, se comprobó el correcto funcionamiento de todas las operaciones CRUD, evidenciando la comunicación entre los servicios.

