import os

from modulos.estruturas.fila import Fila
from modulos.estruturas.lde import LDE
from modulos.estruturas.lse import LSE
from modulos.services.persistencia_service import PersistenciaService

class EstoqueService:
    def __init__(self):
        pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pasta_data = os.path.join(pasta_raiz, "data")

        self.clientes = LSE()
        self.produtos = LDE()
        self.vendas = Fila()
        self.persistencia = PersistenciaService(pasta_data)

        self.carregar_dados()

    def carregar_dados(self):
        for cliente in self.persistencia.carregar_clientes():
            if self.clientes.buscar(cliente.codigo) is None:
                self.clientes.inserir_fim(cliente)

        for produto in self.persistencia.carregar_produtos():
            if self.produtos.buscar(produto.codigo) is None:
                self.produtos.inserir_fim(produto)

        for venda in self.persistencia.carregar_vendas():
            self.vendas.enqueue(venda)

    def gerar_proximo_codigo_cliente(self):
        return self._gerar_proximo_codigo(self.clientes.listar())

    def gerar_proximo_codigo_produto(self):
        return self._gerar_proximo_codigo(self.produtos.listar())

    def gerar_proximo_codigo_venda(self):
        return self._gerar_proximo_codigo(self.vendas.listar())

    def _gerar_proximo_codigo(self, registros):
        maior_codigo = 0

        for registro in registros:
            if registro.codigo > maior_codigo:
                maior_codigo = registro.codigo

        return maior_codigo + 1

    def cadastrar_cliente(self, nome):
        pass

    def listar_clientes(self):
        pass

    def buscar_cliente(self, codigo):
        pass

    def remover_cliente(self, codigo):
        pass

    def cadastrar_produto(self, nome, preco, quantidade):
        pass

    def listar_produtos(self):
        pass

    def listar_produtos_inverso(self):
        pass

    def listar_produtos_ordenados_por_id(self):
        pass

    def buscar_produto(self, codigo):
        pass

    def buscar_produto_binario(self, codigo):
        pass

    def atualizar_estoque(self, codigo, nova_quantidade):
        pass

    def remover_produto(self, codigo):
        pass

    def realizar_venda_exemplo(self, codigo_cliente, codigo_produto, quantidade):
        pass

    def listar_vendas(self):
        pass

    def primeira_venda(self):
        if self.vendas.is_empty():
            return None
        return self.vendas.front()

    def valor_total_estoque(self):
        total = 0.0
        for produto in self.produtos.listar():
            total += produto.preco * produto.quantidade
        return total

    def valor_total_vendas(self):
        total = 0.0
        for venda in self.vendas.listar():
            total += venda.valor_total
        return total

    def clientes_e_valores_totais_gastos(self):
        totais_por_cliente = {}

        for venda in self.vendas.listar():
            codigo = venda.codigo_cliente
            totais_por_cliente[codigo] = totais_por_cliente.get(codigo, 0.0) + venda.valor_total

        resultado = []
        for codigo_cliente, total_gasto in totais_por_cliente.items():
            cliente = self.clientes.buscar(codigo_cliente)
            nome = cliente.nome if cliente else f"Cliente {codigo_cliente} (nao encontrado)"
            resultado.append({"codigo": codigo_cliente, "nome": nome, "total_gasto": total_gasto})

        return resultado

    def cliente_que_mais_gastou(self):
        totais = self.clientes_e_valores_totais_gastos()

        if len(totais) == 0:
            return None

        maior = totais[0]
        for item in totais[1:]:
            if item["total_gasto"] > maior["total_gasto"]:
                maior = item

        return maior

    def produto_mais_vendido(self):
        pass

    def desfazer_ultima_operacao(self):
        pass

    def salvar_clientes(self):
        self.persistencia.salvar_clientes(self.clientes.listar())

    def salvar_produtos(self):
        self.persistencia.salvar_produtos(self.produtos.listar())

    def salvar_vendas(self):
        self.persistencia.salvar_vendas(self.vendas.listar())
