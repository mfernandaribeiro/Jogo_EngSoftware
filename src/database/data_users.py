#pip install pysqlite
import os
import sqlite3
import random

os.remove("users.db") if os.path.exists("users.db") else None

conexao = sqlite3.connect('users.db')
cursor = conexao.cursor()

comando = 'CREATE TABLE USERS (ID INTEGER PRIMARY KEY, NOME VARCHAR(100), SENHA VARCHAR(100))'
cursor.execute(comando)

comando = 'INSERT INTO USERS VALUES (?, ?, ?)'
registros = [(1, 'Fernanda', 'agathachristie123'),
             (2, 'Guilherme', 'harrypotter934'),
             (3, 'John Doe', 'tester372')]

for registro in registros:
    cursor.execute(comando, registro)
conexao.commit()

comando = 'select * from users'
cursor.execute(comando)
dados = cursor.fetchall()

nome_usuario = input("Digite o nome de usuário a ser verificado: ")
cursor.execute('SELECT * FROM users WHERE NOME = ?', (nome_usuario,))
registro = cursor.fetchone()

if registro is not None:
    print("O usuário está registrado.")
else:
    print("O usuário não está registrado.")




