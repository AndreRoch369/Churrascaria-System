def calcular_total_comanda(pedidos):
    return sum(p.calcular_total() for p in pedidos)


def calcular_lucro_diario(comandas):
    return sum(
        calcular_total_comanda(c.pedidos)
        for c in comandas if not c.aberta
    )