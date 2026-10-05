from flask import Flask, send_from_directory
from controllers.produto_controller import obter_produtos, obter_produto_por_id
from controllers.usuario_controller import obter_usuarios, obter_perfil_usuario

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/api/produtos/busca/<string:nome>/<int:pagina>")
def listar_produtos_api(nome, pagina):
    return obter_produtos(nome, pagina)


@app.route("/api/produtos/<int:id>")
def buscar_produto_api(id):
    return obter_produto_por_id(id)


@app.route("/api/usuarios/busca/<string:nome>/<int:pagina>")
def listar_usuarios_api(nome, pagina):
    return obter_usuarios(nome, pagina)


@app.route("/api/usuarios/<int:id>")
def perfil_usuario_api(id):
    return obter_perfil_usuario(id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
