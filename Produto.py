from Estruturas.Fila import Fila

class Produto:

    def __init__(self):
        self.produtos = []

    def cadastrar_produto (self, nome_produto, quantidade_produto, preco_produto, id_produto):
        self.nome_produto = nome_produto
        self.quantidade_produto = quantidade_produto
        self.preco_produto = preco_produto
        self.id_produto = id_produto
        self.produtos.append({
    "id": id_produto,
    "nome": nome_produto,
    "quantidade": quantidade_produto,
    "preco": preco_produto
    })

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        for p in self.produtos:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Quantidade: {p['quantidade']} | Preço: R$ {p['preco']:.2f}")

    def realizar_venda(self, produto_vendido, quantidade_vendida):
        self.produto_vendido = produto_vendido
        self.quantidade_vendida = quantidade_vendida 
        print(f"Venda do produto {self.produto_vendido} realizada com sucesso!")
        self.vendas.enqueue({'Produto': self.produto_vendido, 'Quantidade': self.quantidade_vendida})

    def ver_fila_vendas(self):
        pass

    def desfazer_ultima_operacao(self):
        pass

    def exibir_valor_total_estoque(self):
        pass

    def exibir_valor_total_vendas(self):
        pass
