from Estruturas.Lista import LDE

class Pilha:
    def __init__(self):
        self.pilha = LDE()

    def inserir(self, item):
        """Empilha um item no início da pilha"""
        self.pilha.inserirInicio(item)
    
    def remover(self):
        """Remove e retorna o item do topo da pilha"""
        return self.pilha.removerInicio()
    
    def primeiro(self):
        return self.pilha.primeiro()
    
    def ultimo(self):
        return self.pilha.ultimo()
    
    def imprimir(self):
        return self.pilha.imprimir()
    
    def __str__(self):
        return str(self.pilha)
    def registrar_operacao(self, tipo, dados):
        """
        Registra uma operação na pilha de histórico.
        tipo = "produto", "cliente" ou "venda"
        dados = informações necessárias para desfazer
        """
        self.inserir({"tipo": tipo, "dados": dados})

    def desfazer_ultima_operacao(self, produto, cliente):
        """
        Desfaz a última operação registrada na pilha
        """
        ultima = self.remover()
        if not ultima:
            print("Nenhuma operação para desfazer.")
            return

        tipo = ultima["tipo"]
        dados = ultima["dados"]

        if tipo == "produto":
            produto.remover_produto(dados["id"])
            print(f"Desfeito: cadastro do produto '{dados['nome']}'.")

        elif tipo == "cliente":
            cliente.remover_cliente(dados["id"])
            print(f"Desfeito: cadastro do cliente '{dados['nome']}'.")

        elif tipo == "venda":
            produto.estornar_venda(dados, cliente)
            print("Desfeito: última venda.")

        else:
            print("Tipo de operação desconhecido, não foi possível desfazer.")
