import mysql.connector
from getpass import getpass
from flask import g


senha = getpass("Senha MySQL: ")


def get_connection():
    if "db" not in g:
        g.db = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password=senha,
            database="loja"
        )
    return g.db


def close_connection(exception=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
