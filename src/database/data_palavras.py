#pip install pysqlite
#se não instalar, pip install sqlite5
import os
import sqlite3
import random

def cria_word_data():
    os.remove("palavras.db") if os.path.exists("palavras.db") else None

    conexao = sqlite3.connect('palavras.db')
    cursor = conexao.cursor()

    comando = 'CREATE TABLE PALAVRAS (ID INTEGER PRIMARY KEY, PALAVRA VARCHAR(100), PONTUACAO INTEGER)'
    cursor.execute(comando)

    comando = 'INSERT INTO PALAVRAS VALUES (?, ?, ?)'
    registros = [(1, 'ORNITORRINCO', 3),
                (2, 'PAPAGAIO', 2),
                (3, 'SHOPPING', 2)]

    for registro in registros:
        cursor.execute(comando, registro)
    conexao.commit()

    comando = 'select * from palavras'
    cursor.execute(comando)
    dados = cursor.fetchall()

    cursor.execute('SELECT * FROM palavras ORDER BY RANDOM() LIMIT 1')


    palavra_aleatoria = cursor.fetchone()
    return palavra_aleatoria

#print(palavra_aleatoria[1]) #palavra
#print(palavra_aleatoria[2]) #pontuacoo



