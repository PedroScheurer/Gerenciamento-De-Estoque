class Cliente:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, id_cliente, nome_cliente):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.clientes.append({
            "id": id_cliente,
            "nome": nome_cliente,
            "gasto": 0.0
        })
        
    def listar_cliente(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for p in self.clientes:
            print(f"ID: {p['id']} | Nome: {p['nome']}")

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente['id'] == id_cliente:
                return cliente
        return None
    
    def adicionar_gasto(self, id_cliente, valor):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente["gasto"] += valor

    def listar_clientes_com_gastos(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for p in self.clientes:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Total gasto: R$ {p['gasto']:.2f}")
