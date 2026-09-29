from models.produto import listar_produtos, buscar_produto_por_id


def obter_produtos(nome=None):
    produtos = listar_produtos()

    if nome:
        produtos = [
            produto for produto in produtos
            if nome.lower() in produto["nome"].lower()
        ]

    return produtos


def obter_produto_por_id(id):
    return buscar_produto_por_id(id)