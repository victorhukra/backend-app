
# Dados utilizados apenas para simulação
# enquanto o Banco de Dados ainda não está pronto

produtos = [
    {
        "id": 1,
        "nome": "Mouse Gamer",
        "preco": 150.00
    },
    {   
        "id": 2,
        "nome": "Teclado Mecânico",
        "preco": 250.00
    },
    {
        "id": 3,
        "nome": "Headset Gamer",
        "preco": 200.00
    }
]

def listar_produtos():
    return produtos


def buscar_produto_por_id(id):
    for produto in produtos:
        if produto["id"] == id:
            return produto

    return None