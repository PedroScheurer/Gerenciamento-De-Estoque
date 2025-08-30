from Estruturas.Fila import Fila

class Produto:

    def __init__(self):
        self.produtos = []
        self.vendas = Fila()

    def cadastrar_produto(self, nome_produto, quantidade_produto, preco_produto, id_produto):
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

    def pesquisar_produto(self, termo):
        encontrados = []
        for p in self.produtos:
            if str(p['id']) == str(termo) or termo.lower() in p['nome'].lower():
                encontrados.append(p)
        if not encontrados:
            print("Nenhum produto encontrado.")
        else:
            for p in encontrados:
                print(f"ID: {p['id']} | Nome: {p['nome']} | Quantidade: {p['quantidade']} | Preço (UNID): R$ {p['preco']:.2f}")

    def salvar_estoque(self, arquivo="estoque.txt"):
        with open(arquivo, "w") as f:
            for p in self.produtos:
                f.write(f"{p['id']};{p['nome']};{p['quantidade']};{p['preco']}\n")

    def carregar_estoque(self, arquivo="estoque.txt"):
        try:
            with open(arquivo, "r") as f:
                self.produtos = []
                for linha in f:
                    id_p, nome, qtd, preco = linha.strip().split(";")
                    self.produtos.append({
                        "id": int(id_p),
                        "nome": nome,
                        "quantidade": int(qtd),
                        "preco": float(preco)
                    })
        except FileNotFoundError:
            self.produtos = []

    def retirar_quantidade(self, id_produto, quantidade):
        for p in self.produtos:
            if p['id'] == id_produto:
                if p['quantidade'] < quantidade:
                    raise ValueError("Quantidade insuficiente em estoque")
                p['quantidade'] -= quantidade
                return
        raise ValueError("Produto não encontrado")

    def devolver_quantidade(self, id_produto, quantidade):
        for p in self.produtos:
            if p['id'] == id_produto:
                p['quantidade'] += quantidade
                return
        raise ValueError("Produto não encontrado")

    def realizar_venda(self, id_cliente, id_produto, quantidade_produto, cliente):
        for p in self.produtos:
            if p['id'] == id_produto:
                if p['quantidade'] < quantidade_produto:
                    print("Estoque insuficiente!")
                    return False
                p['quantidade'] -= quantidade_produto
                valor_total = quantidade_produto * p['preco']
                cliente.adicionar_gasto(id_cliente, valor_total)
                self.vendas.inserir({
                    'Produto': id_produto,
                    'Quantidade': quantidade_produto,
                    "Cliente": id_cliente,
                    "Total": valor_total
                })
                print(f"Venda realizada: {quantidade_produto}x {p['nome']} para cliente {id_cliente}")
                return True
        print("Produto não encontrado.")
        return False

    def remover_produto(self, id_produto):
        for p in self.produtos:
            if p["id"] == id_produto:
                self.produtos.remove(p)
                print(f"Produto '{p['nome']}' removido (desfeito).")
                return
        print("Produto não encontrado para remoção.")

    def estornar_venda(self, dados_venda, cliente):
        id_produto = dados_venda["Produto"]
        qtd = dados_venda["Quantidade"]
        valor = dados_venda["Total"]
        id_cliente = dados_venda["Cliente"]
        self.devolver_quantidade(id_produto, qtd)
        cliente.remover_gasto(id_cliente, valor)
        print("Venda estornada com sucesso.")

    def buscar_preco_produto(self, id_produto):
        for p in self.produtos:
            if p['id'] == id_produto:
                return p['preco']
        return None

    def buscar_produto(self, id_produto):
        for produto in self.produtos:
            if produto['id'] == id_produto:
                return produto
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

    def exibir_valor_total_estoque(self):
        total = 0.0
        for p in self.produtos:
            qtd = p["quantidade"]
            preco = p["preco"]
            subtotal = qtd * preco
            total += subtotal
            print(f"ID: {p['id']} | {p['nome']} — {qtd} x R$ {preco:.2f} = R$ {subtotal:.2f}")
        print(f"\nValor total do estoque: R$ {total:.2f}")


