class Comanda:
    def __init__(self, id, mesa):
        self.id = id
        self.mesa = mesa
        self.pedidos = []
        self.aberta = True

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def fechar(self):
        self.aberta = False