from database.connection import get_connection


def listar_produtos(nome, pagina=1):
    limite = 5
    offset = (pagina - 1) * limite

    with get_connection() as cnx:
        with cnx.cursor(dictionary=True) as cur:
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

    for p in produtos:
        p["preco"] = float(p["preco"])

    return produtos


def buscar_produto_por_id(id):
    with get_connection() as cnx:
        with cnx.cursor(dictionary=True) as cur:
            cur.execute(
                "SELECT id, nome, descricao, preco, usuario_id FROM produtos WHERE id = %s",
                (id,)
            )

            produto = cur.fetchone()

    if produto:
        produto["preco"] = float(produto["preco"])

    return produto