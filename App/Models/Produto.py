class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def baixar_estoque(self, quantidade):
        if quantidade > self.estoque:
            raise ValueError("Estoque insuficiente")
        self.estoque -= quantidade