class Cliente:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, id_cliente, nome_cliente):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.clientes.append({
    "id": id_cliente,
    "nome": nome_cliente,
    })
        
    def listar_cliente(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        for p in self.clientes:
            print(f"ID: {p['id']} | Nome: {p['nome']}")
