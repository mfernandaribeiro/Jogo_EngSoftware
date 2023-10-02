import os
import sqlite3

DB_FILE = 'users.db'

def criar_cursor():
    conexao = sqlite3.connect(DB_FILE)
    cursor = conexao.cursor()
    return conexao, cursor

def inicializar_banco_de_dados():
    conexao, cursor = criar_cursor()

    # Check if the USERS table already exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS'")
    table_exists = cursor.fetchone()

    if not table_exists:
        # Create the USERS table
        comando = 'CREATE TABLE USERS (ID INTEGER PRIMARY KEY, USUARIO VARCHAR(100), EMAIL VARCHAR(100), SENHA VARCHAR(100))'
        cursor.execute(comando)

        # Insert sample records
        comando = 'INSERT INTO USERS (ID, USUARIO, EMAIL, SENHA) VALUES (?, ?, ?, ?)'
        registros = [(1, 'Fernanda', 'fernanda@gmail.com', 'agathachristie123'),
                    (2, 'Guilherme', 'guilherme@gmail.com', 'harrypotter934'),
                    (3, 'John Doe', 'johndoe@gmail.com', 'tester372')]

        for registro in registros:
            cursor.execute(comando, registro)

        conexao.commit()

    conexao.close()

if __name__ == "__main__":
    inicializar_banco_de_dados()

