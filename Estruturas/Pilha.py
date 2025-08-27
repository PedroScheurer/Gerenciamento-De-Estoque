from Estruturas.Lista import LDE

class Pilha:
    def __init__(self):
        self.pilha = LDE()
        
    def inserir(self, item):
        self.pilha.inserirInicio(item)
        return
    
    def remover(self):
        self.pilha.removerInicio()
        return
    
    def primeiro(self):
        self.fila.primeiro()
        return
    
    def ultimo(self):
        self.fila.ultimo()
        return
    
    def imprimir(self):
        return self.pilha.imprimir()