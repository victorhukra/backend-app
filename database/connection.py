import mysql.connector
from getpass import getpass


senha = getpass("Senha MySQL: ")


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=senha,
        database="loja"
    )