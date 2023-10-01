#pip install pysqlite
import os
import sqlite3
import random

os.remove("users.db") if os.path.exists("users.db") else None

conexao = sqlite3.connect('users.db')
cursor = conexao.cursor()

comando = 'CREATE TABLE USERS (ID INTEGER PRIMARY KEY, USUARIO VARCHAR(100), EMAIL VARCHAR(100), SENHA VARCHAR(100))'
cursor.execute(comando)

comando = 'INSERT INTO USERS VALUES (?, ?, ?)'
registros = [(1, 'Fernanda', 'fernanda@gmail.com', 'agathachristie123'),
            (2, 'Guilherme', 'guilherme@gmail.com', 'harrypotter934'),
            (3, 'John Doe', 'johndoe@gmail.com', 'tester372')]

for registro in registros:
    cursor.execute(comando, registro)
conexao.commit()

comando = 'select * from users'
cursor.execute(comando)
dados = cursor.fetchall()


def check_user(usuario, senha):
    cursor.execute('SELECT * FROM users WHERE USUARIO = ?', (usuario,))
    registro = cursor.fetchone()

    if registro is not None:
        if registro[3] == senha:
            return True
        else:
            return False
    else:
        return False
    
def check_register(usuario, email, senha, key):
    cursor.execute('SELECT * FROM users WHERE USUARIO = ?', (usuario,))
    registro_user = cursor.fetchone()
    cursor.execute('SELECT * FROM users WHERE EMAIL = ?', (email,))
    registro_email = cursor.fetchone()

    if registro_user is not None:
        return False
    if registro_email is not None:
        return False
    cursor.execute('INSERT INTO USERS (ID, USUARIO, SENHA) VALUES (?, ?)', (key, usuario, senha))
    return True


    
    
    





