from flask import jsonify, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from models.usuario import buscar_usuario_por_email, buscar_usuario_por_id, criar_usuario, listar_usuarios



def obter_usuarios(nome="", pagina=1):
    usuarios = listar_usuarios(nome, pagina)
    return jsonify(usuarios)


def obter_perfil_usuario(id):
    usuario = buscar_usuario_por_id(id)

    if usuario:
        return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404


def cadastrar_usuario():
    pass
    # implementar função 

def iniciar_sessao():
    pass
    # implementar função 

def verificar_sessao():
    pass
    # implementar função 


def encerrar_sessao():
    pass
    # implementar função 
