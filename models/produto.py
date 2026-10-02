from database.connection import get_connection


def listar_produtos(nome, pagina=1):
    limite = 5
    offset = (pagina - 1) * limite

    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)

    cur.execute(
        """
        SELECT id, nome, descricao, preco, usuario_id
        FROM produtos
        WHERE nome LIKE %s
        ORDER BY id
        LIMIT %s OFFSET %s
        """,
        ("%" + nome + "%", limite, offset)
    )

    produtos = cur.fetchall()

    cur.close()
    cnx.close()

    for p in produtos:
        p["preco"] = float(p["preco"])

    return produtos


def buscar_produto_por_id(id):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)

    cur.execute(
        "SELECT id, nome, descricao, preco, usuario_id FROM produtos WHERE id = %s",
        (id,)
    )

    produto = cur.fetchone()

    cur.close()
    cnx.close()

    if produto:
        produto["preco"] = float(produto["preco"])

    return produto