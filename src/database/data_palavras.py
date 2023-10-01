#pip install pysqlite
import os
import sqlite3
import random

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

# Recuperar a palavra aleatória
palavra_aleatoria = cursor.fetchone()


# A palavra aleatória estará na variável 'palavra_aleatoria'
print(palavra_aleatoria[1])



