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
          print("Produto não localizado")

    def remover_produto_completo(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print(f"Produto '{nome}' removido com sucesso.")
            return True
        else:
            print("Produto não encontrado.")
            return False
        
    def listar_produtos_inverso(self):
        itens = list(self.produtos.items())  # [(nome, quantidade), ...]
        return self._inverter_lista(itens)
 
    def _inverter_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
    
    def listar_produtos_ordenados(self):
        itens = list(self.produtos.items())
        self._insertion_sort_por_nome(itens)
        return itens
 
    def _insertion_sort_por_nome(self, lista):
        for i in range(1, len(lista)):
            atual = lista[i]
            j = i - 1
            while j >= 0 and lista[j][0] > atual[0]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = atual

    def buscar_produto_binario(self, nome):
        itens_ordenados = self.listar_produtos_ordenados()
        return self._busca_binaria(itens_ordenados, nome)
 
    def _busca_binaria(self, lista_ordenada, nome):
        inicio = 0
        fim = len(lista_ordenada) - 1
 
        while inicio <= fim:
            meio = (inicio + fim) // 2
            nome_meio, quantidade_meio = lista_ordenada[meio]
 
            if nome_meio == nome:
                return (nome_meio, quantidade_meio)
            elif nome_meio < nome:
                inicio = meio + 1
            else:
                fim = meio - 1
 
        return None