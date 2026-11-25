
from flask import jsonify, request, session # utilizar
from models.produto import criar_produto, listar_produtos, buscar_produto_por_id


def obter_produtos(nome="", pagina=1):
    produtos = listar_produtos(nome, pagina)
    return jsonify(produtos)


def obter_produto_por_id(id):
    produto = buscar_produto_por_id(id)

    if produto:
        return jsonify(produto)

    return jsonify({"erro": "Produto não encontrado"}), 404


def inserir_produto():
    # implementar
    # obs: utilizar a função "criar_produto" do models
