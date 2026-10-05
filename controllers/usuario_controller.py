from flask import jsonify
from models.usuario import listar_usuarios, buscar_usuario_por_id


def obter_usuarios(nome="", pagina=1):
    usuarios = listar_usuarios(nome, pagina)
    return jsonify(usuarios)


def obter_perfil_usuario(id):
    usuario = buscar_usuario_por_id(id)

    if usuario:
        return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404
