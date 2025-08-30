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
                    "id_produto": id_produto,
                    "quantidade": quantidade_produto,
                    "id_cliente": id_cliente,
                    "valor": valor_total
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
        id_produto = dados_venda["id_produto"]
        qtd = dados_venda["quantidade"]
        valor = dados_venda["valor"]
        id_cliente = dados_venda["id_cliente"]
        for p in self.produtos:
            if p["id"] == id_produto:
                p["quantidade"] += qtd
                break
        cliente.remover_gasto(id_cliente, valor)
        print("Venda estornada com sucesso.")

    def buscar_produto(self, id_produto):
        for p in self.produtos:
            if p['id'] == id_produto:
                return p
        return None

    def buscar_nome_produto(self, id_produto):
        produto = self.buscar_produto(id_produto)
        if produto:
            return produto['nome']
        return None

    def buscar_quantidade_produto(self, id_produto):
        produto = self.buscar_produto(id_produto)
        if produto:
            return produto['quantidade']
        return None

    def buscar_preco_produto(self, id_produto):
        produto = self.buscar_produto(id_produto)
        if produto:
            return produto['preco']
        return None

    def pesquisar_produto(self, termo):
        if termo.isdigit():
            produto = self.buscar_produto(int(termo))
            return [produto] if produto else []
        else:
            return [p for p in self.produtos if termo.lower() in p['nome'].lower()]

    def exibir_valor_total_estoque(self):
        total = 0.0
        for p in self.produtos:
            subtotal = p["quantidade"] * p["preco"]
            total += subtotal
            print(f"ID: {p['id']} | {p['nome']} — {p['quantidade']} x R$ {p['preco']:.2f} = R$ {subtotal:.2f}")
        print(f"\nValor total do estoque: R$ {total:.2f}")

    def salvar_estoque(self, arquivo='estoque.txt'):
        with open(arquivo, 'w', encoding='utf-8') as f:
            for p in self.produtos:
                f.write(f"{p['id']};{p['nome']};{p['quantidade']};{p['preco']}\n")

    def carregar_estoque(self, arquivo='estoque.txt'):
        self.produtos = []
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                for linha in f:
                    id_str, nome, qtd_str, preco_str = linha.strip().split(';')
                    self.produtos.append({
                        "id": int(id_str),
                        "nome": nome,
                        "quantidade": int(qtd_str),
                        "preco": float(preco_str)
                    })
        except FileNotFoundError:
            print(f"Arquivo '{arquivo}' não encontrado.")


