from Estruturas.Lista import LDE

class Fila:
    def __init__(self):
        self.fila = LDE()

    def inserir(self, item):
        self.fila.inserirFinal(item)

    def remover(self):
        return self.fila.removerInicio() 

    def primeiro(self):
        return self.fila.primeiro()  

    def ultimo(self):
        return self.fila.ultimo()  

    def imprimir(self):
        self.fila.imprimir()

    def __str__(self):
        return str(self.fila)
