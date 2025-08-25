from Lista import LDE

class Fila:
    def __init__(self):
        self.fila = LDE()

    def inserir(self, item):
        self.fila.inserirFinal(item)
        return
    
    def remover(self):
        self.fila.removerInicio()
        return    

    def primeiro(self):
        self.fila.primeiro()
        return
    
    def ultimo(self):
        self.fila.ultimo()
        return
    
    def imprimir(self):
        return self.fila.imprimir()
    
    def __str__(self):
        return str(self.fila)


filaNormal = LDE()
print(filaNormal)
