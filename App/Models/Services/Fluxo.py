from app.models.pedido import Pedido

def registrar_pedido(comanda, produto, quantidade):
    produto.baixar_estoque(quantidade)
    pedido = Pedido(produto, quantidade)
    comanda.adicionar_pedido(pedido)