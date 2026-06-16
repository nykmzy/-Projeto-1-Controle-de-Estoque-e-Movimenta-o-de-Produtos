import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = os.path.join(BASE_DIR, 'banco', 'estoque.db')

conexao = sqlite3.connect(db_path)

consulta = """
SELECT
    p.nome,
    SUM(
        CASE
            WHEN m.tipo = 'entrada'
            THEN m.quantidade
            ELSE -m.quantidade
        END
    ) AS estoque_atual
FROM Produtos p
JOIN Movimentacoes m
    ON p.id_produto = m.id_produto
GROUP BY p.nome
"""

df = pd.read_sql_query(consulta, conexao)

print(df)

# Criar pasta de gráficos caso não exista
os.makedirs(os.path.join(BASE_DIR, 'graficos'), exist_ok=True)

# Gráfico
plt.figure(figsize=(8, 5))

plt.bar(
    df['nome'],
    df['estoque_atual']
)

plt.title('Estoque Atual dos Produtos')
plt.xlabel('Produto')
plt.ylabel('Quantidade em Estoque')

plt.tight_layout()

grafico_path = os.path.join(BASE_DIR, 'graficos', 'estoque_atual.png')

plt.savefig(grafico_path)

print(f"Gráfico salvo em: {grafico_path}")

conexao.close()