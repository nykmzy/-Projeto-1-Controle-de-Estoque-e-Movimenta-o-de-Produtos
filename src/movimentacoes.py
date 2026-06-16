import sqlite3
import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, 'banco', 'estoque.db')

conexao = sqlite3.connect(db_path)

cursor = conexao.cursor()

movimentacoes = [
    (1, 'entrada', 50, date.today()),
    (1, 'saida', 10, date.today()),

    (2, 'entrada', 100, date.today()),
    (2, 'saida', 25, date.today()),

    (3, 'entrada', 80, date.today()),
    (3, 'saida', 15, date.today()),

    (4, 'entrada', 30, date.today()),
    (4, 'saida', 5, date.today())
]

cursor.executemany("""
INSERT INTO Movimentacoes
(id_produto, tipo, quantidade, data_movimentacao)
VALUES (?, ?, ?, ?)
""", movimentacoes)

conexao.commit()

print("Movimentações registradas com sucesso!")

conexao.close()