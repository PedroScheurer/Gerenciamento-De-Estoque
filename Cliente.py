class Cliente:

    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, id_cliente, nome_cliente):
        self.clientes.append({
            "id": id_cliente,
            "nome": nome_cliente,
            "gasto_total": 0.0
        })

    def listar_cliente(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for c in self.clientes:
            print(f"ID: {c['id']} | Nome: {c['nome']}")

    def listar_clientes_com_gastos(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for c in self.clientes:
            print(f"ID: {c['id']} | Nome: {c['nome']} | Gasto total: R$ {c['gasto_total']:.2f}")

    def buscar_cliente(self, id_cliente):
        for c in self.clientes:
            if c['id'] == id_cliente:
                return c
        return None

    def remover_cliente(self, id_cliente):
        for c in self.clientes:
            if c['id'] == id_cliente:
                self.clientes.remove(c)
                print(f"Cliente '{c['nome']}' removido (desfeito).")
                return
        print("Cliente não encontrado para remoção.")

    def adicionar_gasto(self, id_cliente, valor):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente['gasto_total'] += valor

    def remover_gasto(self, id_cliente, valor):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente['gasto_total'] -= valor
            if cliente['gasto_total'] < 0:
                cliente['gasto_total'] = 0


