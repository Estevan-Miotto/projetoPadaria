from projetoPadaria.produtos import produtos_iniciais

class Estoque:
    def __init__(self):
        self.produtos = produtos_iniciais.copy()

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome] >= quantidade:
                self.produtos[nome] -= quantidade
            else:
                print("Quantidade insuficiente.")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        for nome, quantidade in self.produtos.items():
            print(f"{nome}: {quantidade}")
