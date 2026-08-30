from modulos import clientes
from modulos import produtos

class Estoque:
    def __init__(self):
        self.produtos = produtos.produtos_iniciais.copy()

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

    def buscar_produto(self, nome):
        if nome in self.produtos:
          print(f"Produto: {nome}")
          print(f"Quantidade em estoque: {self.produtos[nome]}")
          return self.produtos[nome]
        else:
         print("Produto não encontrado.")
         return None

    def atualizar_estoque(self, nome, quantidade):
        if nome in self.produtos:
          self.produtos[nome] = quantidade
          print(f"Estoque de {nome} atualizado para {quantidade}.")
        else:
          print("Produto não encontrado.")