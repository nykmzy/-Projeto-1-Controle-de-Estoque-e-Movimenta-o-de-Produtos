import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, 'banco', 'estoque.db')
sql_path = os.path.join(BASE_DIR, 'sql', 'criar_tabelas.sql')

conexao = sqlite3.connect(db_path)

with open(sql_path, 'r', encoding='utf-8') as arquivo:
    script = arquivo.read()

conexao.executescript(script)

print("Banco criado com sucesso!")

conexao.close()