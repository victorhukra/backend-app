from flask import Flask, jsonify, request, send_from_directory
from database.connection import close_connection
from controllers.produto_controller import obter_produtos, obter_produto_por_id
from controllers.usuario_controller import obter_usuarios, obter_perfil_usuario

app = Flask(__name__)

app.teardown_appcontext(close_connection)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")


def obter_pagina():
    valor = request.args.get("pagina", "1")

    try:
        pagina = int(valor)
    except ValueError:
        return None

    return pagina if pagina > 0 else None


@app.route("/api/produtos", methods=["GET"])
def listar_produtos_api():
    pagina = obter_pagina()
    if pagina is None:
        return jsonify({"erro": "O parâmetro 'pagina' deve ser um inteiro positivo"}), 400

    nome = request.args.get("nome", "").strip()
    return obter_produtos(nome, pagina)


@app.route("/api/produtos/<int:id>", methods=["GET"])
def buscar_produto_api(id):
    return obter_produto_por_id(id)


@app.route("/api/usuarios", methods=["GET"])
def listar_usuarios_api():
    pagina = obter_pagina()
    if pagina is None:
        return jsonify({"erro": "O parâmetro 'pagina' deve ser um inteiro positivo"}), 400

    nome = request.args.get("nome", "").strip()
    return obter_usuarios(nome, pagina)


@app.route("/api/usuarios/<int:id>", methods=["GET"])
def perfil_usuario_api(id):
    return obter_perfil_usuario(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
