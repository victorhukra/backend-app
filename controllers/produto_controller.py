from models.produto import listar_produtos, buscar_produto_por_id


def obter_produtos(nome="", pagina=1):
    return listar_produtos(nome, pagina)


def obter_produto_por_id(id):
    return buscar_produto_por_id(id)