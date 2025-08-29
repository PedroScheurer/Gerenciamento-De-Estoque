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
        self.pilha.primeiro()
        return
    
    def ultimo(self):
        self.pilha.ultimo()
        return
    
    def imprimir(self):
        self.pilha.imprimir()
        return 