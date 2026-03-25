import os
import psycopg2 # type: ignore
import psycopg2.extras # type: ignore
from flask import Flask, jsonify, request
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

# Conexión a la base de datos
def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

# Ruta raíz
@app.route("/")
def index():
    return jsonify({
       "message": "API funcionando correctamente",
        "endpoints": {
            "GET /clientes": "Listar clientes",
            "POST /clientes": "Crear cliente",
            "PUT /clientes/<id>": "Actualizar cliente",
            "DELETE /clientes/<id>": "Eliminar cliente",
            "GET /productos": "Listar productos",
            "POST /productos": "Crear producto",
            "PUT /productos/<id>": "Actualizar producto",
            "DELETE /productos/<id>": "Eliminar producto"
        }
    })

# CLIENTES

@app.route("/clientes", methods=["GET"])
def listar_clientes():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM clientes ORDER BY id")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)

@app.route("/clientes/<int:id>", methods=["GET"])
def obtener_cliente(id):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    data = cur.fetchone()
    conn.close()

    if not data:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(data)

@app.route("/clientes", methods=["POST"])
def crear_cliente():
    data = request.get_json()
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(
        "INSERT INTO clientes (nombre, email) VALUES (%s, %s) RETURNING *",
        (data["nombre"], data["email"])
    )

    nuevo = cur.fetchone()
    conn.commit()
    conn.close()
    return jsonify(nuevo), 201

@app.route("/clientes/<int:id>", methods=["PUT"])
def actualizar_cliente(id):
    data = request.get_json()
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(
        "UPDATE clientes SET nombre=%s, email=%s WHERE id=%s RETURNING *",
        (data["nombre"], data["email"], id)
    )

    actualizado = cur.fetchone()
    conn.commit()
    conn.close()

    if not actualizado:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify(actualizado)

@app.route("/clientes/<int:id>", methods=["DELETE"])
def eliminar_cliente(id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM clientes WHERE id=%s RETURNING id", (id,))
    eliminado = cur.fetchone()
    conn.commit()
    conn.close()

    if not eliminado:
        return jsonify({"error": "Cliente no encontrado"}), 404

    return jsonify({"mensaje": "Cliente eliminado correctamente"})


# PRODUCTOS

# PRODUCTOS

@app.route("/productos", methods=["GET"])
def listar_productos():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("SELECT * FROM productos ORDER BY id")
    data = cur.fetchall()
    conn.close()
    return jsonify(data)


@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.get_json()
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(
        "INSERT INTO productos (nombre, precio) VALUES (%s, %s) RETURNING *",
        (data["nombre"], data["precio"])
    )

    nuevo = cur.fetchone()
    conn.commit()
    conn.close()
    return jsonify(nuevo), 201


@app.route("/productos/<int:id>", methods=["PUT", "OPTIONS"])
def actualizar_producto(id):
    if request.method == "OPTIONS":
        return '', 200

    data = request.get_json()
    conn = get_conn()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(
        "UPDATE productos SET nombre=%s, precio=%s WHERE id=%s RETURNING *",
        (data["nombre"], data["precio"], id)
    )

    actualizado = cur.fetchone()
    conn.commit()
    conn.close()

    if not actualizado:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify(actualizado)


@app.route("/productos/<int:id>", methods=["DELETE", "OPTIONS"])
def eliminar_producto(id):
    if request.method == "OPTIONS":
        return '', 200

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("DELETE FROM productos WHERE id=%s RETURNING id", (id,))
    eliminado = cur.fetchone()

    conn.commit()
    conn.close()

    if not eliminado:
        return jsonify({"error": "Producto no encontrado"}), 404

    return jsonify({"mensaje": "Producto eliminado correctamente"})

# Inicio

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)