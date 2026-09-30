# from models.produto import listar_produtos, buscar_produto_por_id


# def obter_produtos(nome=None):
#     produtos = listar_produtos()

#     if nome:
#         produtos = [
#             produto for produto in produtos
#             if nome.lower() in produto["nome"].lower()
#         ]

#     return produtos


# def obter_produto_por_id(id):
#     return buscar_produto_por_id(id)

from models.produto import listar_produtos, buscar_produto_por_id


def obter_produtos(nome="", pagina=1, por_pagina=5):
    produtos = listar_produtos(nome)
    total = len(produtos)
    total_paginas = (total + por_pagina - 1) // por_pagina

    inicio = (pagina - 1) * por_pagina
    fim = inicio + por_pagina

    return {
        "pagina": pagina,
        "total": total,
        "total_paginas": total_paginas,
        "produtos": produtos[inicio:fim]
    }


def obter_produto_por_id(id):
    return buscar_produto_por_id(id)