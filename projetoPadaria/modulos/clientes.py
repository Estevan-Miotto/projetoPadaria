class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Clientes:
    def __init__(self):
        self.clientes = {}
        self.proximo_id = 1

    def cadastrar(self, nome):
        cliente = Cliente(self.proximo_id, nome)
        self.clientes[self.proximo_id] = cliente
        self.proximo_id += 1

    def listar_clientes(self):
        for cliente in self.clientes.values():
            print(f"ID: {cliente.id} | Nome: {cliente.nome}")

    def buscar_cliente(self, codigo):
        return self.clientes.get(codigo)

    def remover_cliente(self, codigo):
        if codigo in self.clientes:
            del self.clientes[codigo]