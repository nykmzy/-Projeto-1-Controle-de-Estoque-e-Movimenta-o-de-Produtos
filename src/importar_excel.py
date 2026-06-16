import pandas as pd
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(BASE_DIR, 'dados', 'produtos.csv')
db_path = os.path.join(BASE_DIR, 'banco', 'estoque.db')

df = pd.read_csv(csv_path, sep=';')

conexao = sqlite3.connect(db_path)

df.to_sql(
    'Produtos',
    conexao,
    if_exists='append',
    index=False
)

print("Produtos importados com sucesso!")

conexao.close()