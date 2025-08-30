from Estruturas.DNodo import DNodo

class LDE:
    def __init__(self):
        self.header = DNodo()
        self.trailer = DNodo()
        self.tamanho = 0

    def estaVazia(self):
        return self.tamanho == 0

    def _inserirPrimeiro(self, item):
        if item is None or item == "":
            print("Insira um item válido")
            return
        nodo = DNodo(item)
        self.header.proximo = nodo
        self.trailer.anterior = nodo
        nodo.proximo = self.trailer
        nodo.anterior = self.header
        self.tamanho = 1

    def _removerUnico(self):
        if self.estaVazia():
            print("A lista já está vazia")
            return None
        if self.tamanho == 1:
            removido = self.header.proximo
            self.header.proximo = None
            self.trailer.anterior = None
            removido.proximo = None
            removido.anterior = None
            self.tamanho = 0
            return removido.dado

    def inserirInicio(self, item):
        if self.estaVazia():
            self._inserirPrimeiro(item)
            return
        if item is None or item == "":
            print("Insira um item válido")
            return
        nodo = DNodo(item)
        antigoPrimeiro = self.header.proximo
        antigoPrimeiro.anterior = nodo
        self.header.proximo = nodo
        nodo.anterior = self.header
        nodo.proximo = antigoPrimeiro
        self.tamanho += 1

    def removerInicio(self):
        if self.tamanho <= 1:
            return self._removerUnico()
        removido = self.header.proximo
        novoPrimeiro = removido.proximo
        self.header.proximo = novoPrimeiro
        novoPrimeiro.anterior = self.header
        removido.proximo = None
        removido.anterior = None
        self.tamanho -= 1
        return removido.dado

    def inserirFinal(self, item):
        if self.estaVazia():
            self._inserirPrimeiro(item)
            return
        if item is None or item == "":
            print("Insira um item válido")
            return
        nodo = DNodo(item)
        antigoUltimo = self.trailer.anterior
        antigoUltimo.proximo = nodo
        nodo.anterior = antigoUltimo
        nodo.proximo = self.trailer
        self.trailer.anterior = nodo
        self.tamanho += 1

    def removerFinal(self):
        if self.tamanho <= 1:
            return self._removerUnico()
        removido = self.trailer.anterior
        novoUltimo = removido.anterior
        novoUltimo.proximo = self.trailer
        self.trailer.anterior = novoUltimo
        removido.proximo = None
        removido.anterior = None
        self.tamanho -= 1
        return removido.dado

    def primeiro(self):
        if self.estaVazia():
            print("A lista está vazia")
            return None
        return self.header.proximo.dado

    def ultimo(self):
        if self.estaVazia():
            print("A lista está vazia")
            return None
        return self.trailer.anterior.dado

    def imprimir(self):
        if self.estaVazia():
            print("A lista está vazia")
            return
        item = self.header.proximo
        while item != self.trailer:
            print(item.dado)
            item = item.proximo

    def removerEspecifico(self, dado_a_ser_removido):
        if self.estaVazia():
            print("A lista está vazia")
            return
        item = self.header.proximo
        encontrado = False
        while item != self.trailer:
            if item.dado == dado_a_ser_removido:
                item.anterior.proximo = item.proximo
                item.proximo.anterior = item.anterior
                item.proximo = None
                item.anterior = None
                self.tamanho -= 1
                encontrado = True
                break
            item = item.proximo
        if encontrado:
            print("Dado deletado com sucesso")
        else:
            print("Dado não encontrado na lista")

    def __str__(self):
        if self.estaVazia():
            return "Lista vazia"
        elementos = []
        atual = self.header.proximo
        while atual != self.trailer:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos)


