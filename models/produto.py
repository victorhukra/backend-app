from contextlib import closing
from database.connection import get_connection


def listar_produtos(nome, pagina=1):
    limite = 5
    offset = (pagina - 1) * limite

    cnx = get_connection()

    with closing(cnx.cursor(dictionary=True)) as cur:
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
    cnx = get_connection()

    with closing(cnx.cursor(dictionary=True)) as cur:
        cur.execute(
            """
            SELECT id, nome, descricao, preco, usuario_id
            FROM produtos
            WHERE id = %s
            """,
            (id,)
        )

        produto = cur.fetchone()

    if produto:
        produto["preco"] = float(produto["preco"])

    return produto


def criar_produto(nome, descricao, preco, usuario_id):
    cnx = get_connection()

    with closing(cnx.cursor()) as cur:
        try:
            cur.execute(
                """
                INSERT INTO produtos (nome, descricao, preco, usuario_id)
                VALUES (%s, %s, %s, %s)
                """,
                (nome, descricao, preco, usuario_id)
            )
            cnx.commit()
            return cur.lastrowid
        except Exception:   
            cnx.rollback() 
            raise
