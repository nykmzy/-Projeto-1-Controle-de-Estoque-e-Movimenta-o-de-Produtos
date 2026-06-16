CREATE TABLE Produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT,
    preco REAL
);

CREATE TABLE Movimentacoes (
    id_movimentacao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER,
    tipo TEXT,
    quantidade INTEGER,
    data_movimentacao DATE,
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);