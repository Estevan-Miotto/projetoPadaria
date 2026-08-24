from cliente import Cliente

class Clientes:

    def __init__(self):
        self.clientes = {}
        self.proximo_id = 1

    def cadastrar(self, nome):

        cliente = Cliente(self.proximo_id, nome)


        self.clientes[self.proximo_id] = cliente

        self.proximo_id += 1

    def listar(self):

        for cliente in self.clientes.values():
            print(f"ID: {cliente.id} | "f"Nome: {cliente.nome}")