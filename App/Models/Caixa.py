class Caixa:
    def __init__(self):
        self.aberto = False
        self.total = 0

    def abrir(self):
        self.aberto = True

    def fechar(self):
        self.aberto = False