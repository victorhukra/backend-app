import re

from flask import jsonify, request, session
from mysql.connector.errors import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from models.usuario import (
    buscar_usuario_por_email,
    buscar_usuario_por_id,
    criar_usuario,
    listar_usuarios,
)


_EMAIL_RE = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")
_TAMANHO_MAXIMO_SENHA = 128


def obter_usuarios(nome="", pagina=1):
    usuarios = listar_usuarios(nome, pagina)
    return jsonify(usuarios)


def obter_perfil_usuario(id):
    usuario = buscar_usuario_por_id(id)

    if usuario:
        return jsonify(usuario)

    return jsonify({"erro": "Usuário não encontrado"}), 404


def cadastrar_usuario():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "O corpo da requisição deve ser um objeto JSON."}), 400

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    if not isinstance(nome, str) or not nome.strip() or len(nome.strip()) > 100:
        return jsonify({"erro": "Informe um nome com até 100 caracteres."}), 400

    if not isinstance(email, str):
        return jsonify({"erro": "Informe um endereço de e-mail válido."}), 400

    email = email.strip().lower()
    if len(email) > 150 or not _EMAIL_RE.fullmatch(email):
        return jsonify({"erro": "Informe um endereço de e-mail válido."}), 400

    if not isinstance(senha, str) or len(senha) < 8 or len(senha) > _TAMANHO_MAXIMO_SENHA:
        return jsonify({"erro": "A senha deve ter entre 8 e 128 caracteres."}), 400

    if buscar_usuario_por_email(email):
        return jsonify({"erro": "Já existe um usuário cadastrado com este e-mail."}), 409

    senha_hash = generate_password_hash(senha)

    try:
        usuario_id = criar_usuario(nome.strip(), email, senha_hash)
    except IntegrityError:
        # Protege também contra duas requisições concorrentes para o mesmo e-mail.
        return jsonify({"erro": "Já existe um usuário cadastrado com este e-mail."}), 409

    return jsonify({"id": usuario_id, "mensagem": "Usuário cadastrado com sucesso."}), 201


def iniciar_sessao():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "O corpo da requisição deve ser um objeto JSON."}), 400

    email = dados.get("email")
    senha = dados.get("senha")

    if not isinstance(email, str) or not email.strip() or len(email.strip()) > 150:
        return jsonify({"erro": "Informe um endereço de e-mail válido."}), 400

    if not isinstance(senha, str) or not senha:
        return jsonify({"erro": "Informe a senha."}), 400

    usuario = buscar_usuario_por_email(email.strip().lower())

    # Usuários criados antes da migração podem ainda não ter senha definida.
    if (
        usuario is None
        or not usuario.get("senha_hash")
        or not check_password_hash(usuario["senha_hash"], senha)
    ):
        return jsonify({"erro": "E-mail ou senha inválidos."}), 401

    session.clear()
    session["usuario_id"] = usuario["id"]
    session["usuario_nome"] = usuario["nome"]

    return jsonify({
        "autenticado": True,
        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"],
        },
    }), 200


def verificar_sessao():
    usuario_id = session.get("usuario_id")

    if usuario_id is None:
        return jsonify({"autenticado": False}), 200

    return jsonify({
        "autenticado": True,
        "usuario": {
            "id": usuario_id,
            "nome": session.get("usuario_nome"),
        },
    }), 200


def encerrar_sessao():
    session.clear()
    return jsonify({"autenticado": False, "mensagem": "Sessão encerrada com sucesso."}), 200
