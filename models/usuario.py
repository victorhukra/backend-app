from contextlib import closing
from database.connection import get_connection


def listar_usuarios(nome, pagina=1):
    limite = 5
    offset = (pagina - 1) * limite

    cnx = get_connection()

    with closing(cnx.cursor(dictionary=True)) as cur:
        cur.execute(
            """
            SELECT id, nome, email
            FROM usuarios
            WHERE nome LIKE %s
            ORDER BY id
            LIMIT %s OFFSET %s
            """,
            ("%" + nome + "%", limite, offset)
        )

        usuarios = cur.fetchall()

    return usuarios


def buscar_usuario_por_id(id):
    cnx = get_connection()

    with closing(cnx.cursor(dictionary=True)) as cur:
        cur.execute(
            """
            SELECT id, nome, email
            FROM usuarios
            WHERE id = %s
            """,
            (id,)
        )

        usuario = cur.fetchone()

        if usuario is None:
            return None

        cur.execute(
            """
            SELECT id, nome, descricao, preco
            FROM produtos
            WHERE usuario_id = %s
            ORDER BY id
            """,
            (id,)
        )

        produtos = cur.fetchall()

    for produto in produtos:
        produto["preco"] = float(produto["preco"])

    usuario["produtos"] = produtos

    return usuario


def buscar_usuario_por_email(email):
    cnx = get_connection()

    with closing(cnx.cursor(dictionary=True)) as cur:
        cur.execute(
            """
            SELECT id, nome, email, senha_hash
            FROM usuarios
            WHERE email = %s
            """,
            (email,)
        )

        return cur.fetchone()


def criar_usuario(nome, email, senha_hash):
    cnx = get_connection()

    with closing(cnx.cursor()) as cur:
        try:
            cur.execute(
                """
                INSERT INTO usuarios (nome, email, senha_hash)
                VALUES (%s, %s, %s)
                """,
                (nome, email, senha_hash)
            )
            cnx.commit()
            return cur.lastrowid
        except Exception:
            cnx.rollback()
            raise
