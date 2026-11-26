from flask import jsonify, request, session
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
    ''' Valida os dados recebidos e cadastra um produto vinculado ao usuário autenticado. '''

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({"erro": "O corpo da requisição deve ser um objeto JSON"}), 400

    nome = dados.get("nome")
    descricao = dados.get("descricao", "")
    valor = dados.get("preco")

    if not isinstance(nome, str) or not nome.strip() or len(nome.strip()) > 150:
        return jsonify({"erro": "Informe um nome com até 150 caracteres."}), 400
    
    if not isinstance(descricao, str) or len(descricao) > 10000:
        return jsonify({"erro": "A descrição deve ter até 10000 caracteres."}), 400
    
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        return jsonify({"erro": "Informe o preço como um número."}), 400

    try:
        preco = float(valor)
    except (TypeError, ValueError):
        return jsonify({"erro": "Informe um preço numérico."}), 400

    if not 0 < preco <= 99999999.99:
        return jsonify({"erro": "O preço deve ser maior que zero e não pode ultrapassar 99999999.99."}), 400

    produto_id = criar_produto(nome.strip(), descricao.strip(), preco, session["usuario_id"])

    return jsonify({"id": produto_id, "mensagem": "Produto foi cadastrado com sucesso!"}), 201
