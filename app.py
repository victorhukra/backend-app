from flask import Flask
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

@app.route("/produtos")
def listar_produtos():
    return "Lista de produtos"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)