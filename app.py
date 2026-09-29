
from flask import Flask, jsonify, request
from controllers.produto_controller import obter_produtos, obter_produto_por_id

app = Flask(__name__)


@app.route("/usuarios")
def listar_usuarios():
    return "Lista de usuários"

# Rota para listar os produtos cadastrados e retornar os dados em formato JSON
@app.route("/api/produtos/<string:nome>", methods=["GET"])
def listar_produtos_api(nome):
    produtos = obter_produtos(nome)

    return jsonify(produtos)

# Rota para listar os produtos cadastrados por ID 

@app.route("/api/produtos/<int:id>")
def buscar_produto_api(id):
    produto = obter_produto_por_id(id)

    if produto is None:
        return jsonify({"erro": "Produto não encontrado"}), 404

    return jsonify(produto)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
