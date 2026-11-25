from functools import wraps

from flask import jsonify, session


def login_required(func):
    @wraps(func)
    def verificar_autenticacao(*args, **kwargs):
        if "usuario_id" not in session:
            return jsonify({"erro": "Usuário não autenticado"}), 401

        return func(*args, **kwargs)

    return verificar_autenticacao
