from database.connection import get_connection

def listar_usuarios(nome, pagina=1):
    limite = 5
    offset = (pagina - 1) * limite

    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)

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

    cur.close()
    cnx.close()

    return usuarios


def buscar_usuario_por_id(id):
    cnx = get_connection()
    cur = cnx.cursor(dictionary=True)

    cur.execute(
        """SELECT id, nome, email FROM usuarios WHERE id = %s""", (id,))

    usuario = cur.fetchone()

    if usuario is None:
        cur.close()
        cnx.close()
        return None

    cur.execute("""SELECT id, nome, descricao, preco FROM produtos WHERE usuario_id = %s ORDER BY id""", (id,))

    produtos = cur.fetchall()

    cur.close()
    cnx.close()

    for produto in produtos:
        produto["preco"] = float(produto["preco"])

    usuario["produtos"] = produtos

    return usuario