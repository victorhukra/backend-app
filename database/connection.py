import mysql.connector
# Estrutura para iniciar a conexão com o banco de dados MySQL
# que será alterado de acordo com a conexão a ser estabelecida.
# (coletado do site da biblioteca mysql-connector-python)

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mike",
    password="s3cre3t!")

cur = cnx.cursor()

cur.execute("SELECT CURDATE()")

row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

cnx.close()