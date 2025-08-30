from Estruturas.Lista import LDE

class Pilha:
    def __init__(self):
        self.pilha = LDE()

    def inserir(self, item):
        self.pilha.inserirInicio(item)

    def remover(self):
        nodo = self.pilha.removerInicio()
        return nodo  

    def primeiro(self):
        return self.pilha.primeiro()

    def ultimo(self):
        return self.pilha.ultimo()

    def imprimir(self):
        self.pilha.imprimir()

    def __str__(self):
        return str(self.pilha)


