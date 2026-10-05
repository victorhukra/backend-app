from flask import jsonify
from models.produto import listar_produtos, buscar_produto_por_id


def obter_produtos(nome="", pagina=1):
    produtos = listar_produtos(nome, pagina)
    return jsonify(produtos)


def obter_produto_por_id(id):
    produto = buscar_produto_por_id(id)

    if produto:
        return jsonify(produto)

    return jsonify({"erro": "Produto não encontrado"}), 404
