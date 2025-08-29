from Estruturas.Fila import Fila

class Produto:

    def __init__(self):
        self.produtos = []
        self.vendas = Fila()

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
            print(f"ID: {p['id']} | Nome: {p['nome']} | Quantidade: {p['quantidade']} | Preço (UNID): R$ {p['preco']:.2f}")

    def realizar_venda(self, id_cliente, id_produto, quantidade_produto):
        self.id_produto = id_produto
        self.quantidade_produto = quantidade_produto 
        self.vendas.inserir({
            'Produto': self.id_produto,
            'Quantidade': self.quantidade_produto,
            "Cliente": id_cliente
        })
    
    def buscar_preco_produto(self, id_produto):
        for p in self.produtos:
            if p['id'] == id_produto:
                return p['preco']
        return None
    
    def buscar_produto(self, id_produto):
        for produto in self.produtos:
            if produto['id'] == id_produto:
                return produto['id']
        return None
    
    def buscar_quantidade_produto(self, id_produto):
        for produto in self.produtos:
            if produto['id'] == id_produto:
                return produto['quantidade']
        return None
    
    def buscar_nome_produto(self, id_produto):
        for produto in self.produtos:
            if produto['id'] == id_produto:
                return produto['nome']
        return None

    def ver_fila_vendas(self):
        pass

    def desfazer_ultima_operacao(self):
        pass

    def exibir_valor_total_estoque(self):
        total = 0.0
        for p in self.produtos:
            qtd = p["quantidade"]
            preco = p["preco"]
            subtotal = qtd * preco
            total += subtotal
            print(f"ID: {p['id']} | {p['nome']} — {qtd} x R$ {preco:.2f} = R$ {subtotal:.2f}")
        print(f"\nValor total do estoque: R$ {total:.2f}")
    
    def exibir_valor_total_vendas(self):
        total = 0.0

    def exbir_clientes_valores_totais_gastos(self):
        pass

