from database.connection import get_connection

def listar_usuarios(nome, pagina=1):
    limite = 5
    offset = (pagina - 1) * limite

    with get_connection() as cnx:
        with cnx.cursor(dictionary=True) as cur:
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
    with get_connection() as cnx:
        with cnx.cursor(dictionary=True) as cur:
            cur.execute(
                "SELECT id, nome, email FROM usuarios WHERE id = %s", (id,))

            usuario = cur.fetchone()

            if usuario is None:
                return None

            cur.execute(
                "SELECT id, nome, descricao, preco FROM produtos WHERE usuario_id = %s ORDER BY id",
                (id,)
            )

            produtos = cur.fetchall()

    for produto in produtos:
        produto["preco"] = float(produto["preco"])

    usuario["produtos"] = produtos

    return usuario