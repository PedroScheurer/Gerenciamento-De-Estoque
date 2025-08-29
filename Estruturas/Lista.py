from Estruturas.DNodo import DNodo

class LDE:
    def __init__(self):
        self.header = DNodo()
        self.trailer = DNodo()
        self.tamanho = 0

    def estaVazia(self):
        if(self.tamanho == 0):
            return True
        
        return False

    def _inserirPrimeiro(self, item):
        if(item == None or item == ""):
            return print("Insira um item válido")
        item = DNodo(item)
        self.header.proximo = item
        self.trailer.anterior = item
        
        item.proximo = self.trailer
        item.anterior = self.header
        self.tamanho = 1
        return
    
    def _removerUnico(self):
        if(self.estaVazia()):
                print("A lista já está vazia")
                return None
        
        if self.tamanho == 1:
            removido = self.header.proximo
            self.header.proximo = None
            self.trailer.anterior = None
            
            removido.anterior = None
            removido.proximo = None
            self.tamanho = 0
            return removido

    def inserirInicio(self, item):
        if(self.estaVazia()):
            self._inserirPrimeiro(item)
            return
        
        if(item == None or item == ""):
            return print("Insira um item válido")
        
        item = DNodo(item)
        antigoPrimeiro = self.header.proximo
        antigoPrimeiro.anterior = item
        self.header.proximo = item
        
        item.anterior = self.header
        item.proximo = antigoPrimeiro
        self.tamanho += 1
        return
    
    def removerInicio(self):
        if(self.tamanho <= 1):
            return self._removerUnico()
        
        removido = self.header.proximo
        novoPrimeiro = removido.proximo
        
        self.header.proximo = novoPrimeiro
        novoPrimeiro.anterior = self.header
        
        removido.proximo = None
        removido.anterior = None
        
        self.tamanho -= 1
        return
    

    def inserirFinal(self, item):
        if(self.estaVazia()):
            self._inserirPrimeiro(item)
            return
        
        if(item == None or item == ""):
            return print("Insira um item válido")
        
        item = DNodo(item)
        antigoUltimo = self.trailer.anterior
        antigoUltimo.proximo = item
        item.proximo = self.trailer
        
        item.anterior = antigoUltimo
        self.trailer.anterior = item
        self.tamanho += 1
        return

    def removerFinal(self):
        if self.tamanho <= 1:
            return self._removerUnico()
        
        removido = self.trailer.anterior
        novo_trailer = removido.anterior

        removido.proximo = None
        removido.anterior = None

        novo_trailer.proximo = self.trailer
        self.trailer.anterior = novo_trailer

        self.tamanho -= 1

        return removido
        
    def imprimir(self):
        if(self.estaVazia()):
            print("A lista está vazia")
            return
        
        item = self.header.proximo
        while item != self.trailer:
            print(item)
            item = item.proximo

    def imprimirEmLinha(self):
        if(self.estaVazia()):
            print("A lista está vazia")
            return
        
        item = self.header.proximo

        valorAImprimir = ""
        while item != self.trailer:
            if item == self.header.proximo:
                valorAImprimir = f"[HEADER] => [{item}]"
            else:
                valorAImprimir += f" => [{item}]"

            item = item.proximo
        
        valorAImprimir += " <= [TRAILER]"

        print(valorAImprimir)

    def __str__(self):
        if self.estaVazia():
            return "Lista vazia"
    
        elementos = []
        atual = self.header.proximo
        while atual != self.trailer:
            elementos.append(str(atual.dado))
            atual = atual.proximo

        return " -> ".join(elementos)

    def primeiro(self):
        if(self.estaVazia()):
            print("A lista está vazia")
            return
        
        return self.header.proximo

    def ultimo(self):
        if(self.estaVazia()):
            print("A lista está vazia")
            return
        
        return self.trailer.anterior

    def removerEspecifico(self, dado_a_ser_removido):
        if(self.estaVazia()):
            print("A lista está vazia")
            return
        
        item = DNodo(item)
        item = self.header.proximo

        contem_o_dado = False
        
        while item != self.trailer:
            if item.dado == dado_a_ser_removido:
                proximo_atual = item.proximo
                proximo_anterior = item.anterior

                item.proximo = None
                item.anterior = None

                proximo_anterior.proximo = proximo_atual
                proximo_atual.anterior = proximo_anterior
                contem_o_dado = True
                self.tamanho -= 1
                break

            item = item.proximo

        if contem_o_dado is False:
            print("Dado não encontrado na lista")
        else:
            print("Dado deletado com sucesso")
