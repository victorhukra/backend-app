
from flask import Flask, jsonify
from controllers.produto_controller import obter_produtos


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route("/usuarios")
def listar_usuarios():
    return "Lista de usuários"

@app.route("/usuarios")
def criar_usuario():
    return "Usuário criado"

# Rota para listar os produtos cadastrados e retornar os dados em formato JSON
@app.route("/api/produtos", methods=["GET"])
def listar_produtos_api():
    produtos = obter_produtos()
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)