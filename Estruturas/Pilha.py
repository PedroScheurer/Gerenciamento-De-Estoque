from Estruturas.Lista import LDE

class Pilha:
    def __init__(self):
        self.pilha = LDE()
        
    def inserir(self, item):
        self.pilha.inserirInicio(item)
        return
    
    def remover(self):
        return self.pilha.removerInicio()
    
    def primeiro(self):
        return self.pilha.primeiro()
    
    def ultimo(self):
        return self.pilha.ultimo()
    
    def imprimir(self):
        return self.pilha.imprimir()
    
    def __str__(self):
        return str(self.pilha)
