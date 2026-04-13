CREATE TABLE produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    estoque INTEGER
);

CREATE TABLE mesa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero INTEGER
);

CREATE TABLE comanda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mesa_id INTEGER,
    aberta BOOLEAN,
    FOREIGN KEY (mesa_id) REFERENCES mesa(id)
);

CREATE TABLE pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comanda_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY (comanda_id) REFERENCES comanda(id),
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);