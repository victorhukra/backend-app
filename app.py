from flask import Flask, jsonify
from controllers.produto_controller import obter_produtos, obter_produto_por_id
from controllers.usuario_controller import obter_usuarios, obter_perfil_usuario

app = Flask(__name__)


@app.route("/api/produtos/busca/<string:nome>/<int:pagina>")
def listar_produtos_api(nome, pagina):
    produtos = obter_produtos(nome, pagina)
    return jsonify(produtos)


@app.route("/api/produtos/<int:id>")
def buscar_produto_api(id):
    produto = obter_produto_por_id(id)

    if produto:
        return jsonify(produto)

    return jsonify({"erro": "Produto não encontrado"}), 404


@app.route("/api/usuarios/busca/<string:nome>/<int:pagina>")
def listar_usuarios_api(nome, pagina):
    usuarios = obter_usuarios(nome, pagina)
    return jsonify(usuarios)


@app.route("/api/usuarios/<int:id>")
def perfil_usuario_api(id):
    usuario = obter_perfil_usuario(id)

    if usuario:
        return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)


    