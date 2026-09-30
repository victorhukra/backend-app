# from flask import Flask, jsonify, request
# from controllers.produto_controller import obter_produtos, obter_produto_por_id


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello"

# @app.route("/usuarios")
# def listar_usuarios():
#     return "Lista de usuários"

# @app.route("/usuarios")
# def criar_usuario():
#     return "Usuário criado"

# # Rota para listar os produtos cadastrados e retornar os dados em formato JSON
# @app.route("/api/produtos", methods=["GET"])
# def listar_produtos_api():
#     nome = request.args.get("nome")
#     produtos = obter_produtos(nome)

#     return jsonify(produtos)

# # Rota para listar os produtos cadastrados por ID 

# @app.route("/api/produtos/<int:id>")
# def buscar_produto_api(id):
#     produto = obter_produto_por_id(id)

#     if produto is None:
#         return jsonify({"erro": "Produto não encontrado"}), 404

#     return jsonify(produto)

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=3000, debug=True)

from flask import Flask, jsonify, request
from controllers.produto_controller import obter_produtos, obter_produto_por_id
# from controllers.usuario_controller import obter_usuarios, obter_perfil
app = Flask(__name__, static_folder="static", static_url_path="/static")


@app.route("/")
def home():
    return app.send_static_file("index.html")



# Lista produtos com paginação e busca: /api/produtos?nome=mouse&pagina=1&por_pagina=5
@app.route("/api/produtos")
def listar_produtos_api():
    nome = request.args.get("nome", "")
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = request.args.get("por_pagina", 5, type=int)
    return jsonify(obter_produtos(nome, pagina, por_pagina))

# Rota para listar os produtos cadastrados e retornar os dados em formato JSON
# @app.route("/api/produtos/<string:nome>", methods=["GET"])
# def listar_produtos_api(nome):
#     produtos = obter_produtos(nome)
# >>>>>>> 8bbf525c8686488bd3afccadc76825c711af1d85


# Rota parametrizada com String: /api/produtos/busca/mouse
@app.route("/api/produtos/busca/<string:termo>")
def buscar_por_termo_api(termo):
    pagina = request.args.get("pagina", 1, type=int)
    return jsonify(obter_produtos(termo, pagina))


# Produto por ID: /api/produtos/1
@app.route("/api/produtos/<int:id>")
def buscar_produto_api(id):
    produto = obter_produto_por_id(id)
    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404
    return jsonify(produto)

# # Lista de usuários: /api/usuarios
# @app.route("/api/usuarios")
# def listar_usuarios_api():
#     return jsonify(obter_usuarios())


# # Perfil do usuário com seus produtos: /api/usuarios/1
# @app.route("/api/usuarios/<int:id>")
# def perfil_usuario_api(id):
#     perfil = obter_perfil(id)
#     if perfil is None:
#         return jsonify({"erro": "Usuário não encontrado"}), 404
#     return jsonify(perfil)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=3000, debug=True)
# >>>>>>> 8bbf525c8686488bd3afccadc76825c711af1d85
A