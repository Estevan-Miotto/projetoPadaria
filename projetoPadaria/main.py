
import os

from modulos.operacoes.clientes import cadastrar_cliente, listar_clientes, buscar_cliente, remover_cliente

from modulos.operacoes.produtos import (
    cadastrar_produto,
    listar_produtos, buscar_produto,
    atualizar_estoque, remover_produto,
    listar_produtos_inverso,
    listar_produtos_ordenados_por_id,
    buscar_produto_binario,
    realizar_venda)

from modulos.services.estoque_service import EstoqueService
from modulos.recursos import (
    limpar_terminal,
    ler_texto_obrigatorio,
    mostrar_menu)
from modulos.models.cliente import Cliente
from modulos.services.persistencia_service import PersistenciaService

pasta_data = os.path.join(
    os.path.dirname(__file__),"modulos","data")

persistencia = PersistenciaService(pasta_data)
service = EstoqueService()
clientes = persistencia.carregar_clientes()
produtos = persistencia.carregar_produtos()

while True:
    limpar_terminal()
    opcao = mostrar_menu()

    if opcao == "1":#Cadastrar cliente
        cadastrar_cliente(clientes, persistencia)

    elif opcao == "2":
        listar_clientes(clientes)

    elif opcao == "3":
        buscar_cliente(clientes)

    elif opcao == "4":
        remover_cliente(clientes, persistencia)

    elif opcao == "5":
        cadastrar_produto(produtos, persistencia)

    elif opcao == "6":
        listar_produtos(produtos)

    elif opcao == "7":
        buscar_produto(produtos)

    elif opcao == "8":
        atualizar_estoque(produtos, service)

    elif opcao == "9":
        remover_produto(produtos, persistencia)

    elif opcao == "10":
        listar_produtos_inverso(service)

    elif opcao == "11":
        listar_produtos_ordenados_por_id(service)

    elif opcao == "12":
        buscar_produto_binario(produtos)

    elif opcao == '13':
        realizar_venda(produtos, service)

    elif opcao == '14': #Listar vendas
        print("Fila de vendas:")
        vendas = service.listar_vendas()
        for venda in vendas:
            print(f"Cliente: {venda['cliente'].nome} | Produto: {venda['produto'].nome} | Quantidade: {venda['quantidade']}")

    elif opcao == '15': #Cadastrar pedido
        venda = service.primeira_venda()
        if venda:
            print(venda)
        else:
            print("Não há vendas na fila.")

    elif opcao == '16': #Listar pedidos
        total = service.valor_total_estoque()
        print(f"Valor total do estoque: R$ {total:.2f}")

    elif opcao == '17': #Exibir valor total das vendas
        total = service.valor_total_vendas()
        print(f"Valor total das vendas: R$ {total:.2f}")

    elif opcao == '18': #cliente com valor gasto 
        print("Clientes e valores totais gastos:")
        totais = service.clientes_e_valores_totais_gastos()

        if len(totais) == 0:
            print("Nenhuma venda registrada!!")

        else:
            for item in totais:
                print(f"Cliente:{item['nome']} | Total gasto: R${item[' total_gasto']:.2f}")

    elif opcao == '19': #cliente que mais gastou 
        maior = service.cliente_que_mais_gastou()
        if maior is None:
            print(" Nenhuma venda registrada ainda. ")
        else:
            print(f"Cliente que mais gastou: {maior['nome']} - total: R${maior['total_gasto']:.2f}")

    elif opcao == '20': #Exibit produto mais vendido
        produto_mais_vendido = estoque.produto_mais_vendido()
        if produto_mais_vendido:
            print(f"Produto mais vendido: {produto_mais_vendido.nome} - Quantidade vendida: {produto_mais_vendido.quantidade_vendida}")
        else:
            print("Nenhum produto vendido ainda.")

    elif opcao == '21':  # Desfazer ultima operacao
        operacao = historico.desempilhar()
        if operacao is None:
            print("Não há operações para desfazer.")
        else:
            tipo = operacao["tipo"]

            if tipo == "cadastro_cliente":
                clientes.remover_cliente(operacao["id"])
                print(f"Cadastro do cliente ID {operacao['id']} desfeito.")

            elif tipo == "remocao_cliente":
                clientes.reinserir(operacao["id"], operacao["nome"])
                print(f"Remoção do cliente '{operacao['nome']}' desfeita.")

            elif tipo == "cadastro_produto":
                if operacao["quantidade_anterior"] is None:
                    if operacao["nome"] in estoque.produtos:
                        del estoque.produtos[operacao["nome"]]
                else:
                    estoque.produtos[operacao["nome"]] = operacao["quantidade_anterior"]
                print(f"Cadastro do produto '{operacao['nome']}' desfeito.")

            elif tipo == "atualizacao_estoque":
                estoque.produtos[operacao["nome"]] = operacao["quantidade_anterior"]
                print(f"Atualização de estoque de '{operacao['nome']}' desfeita.")

            elif tipo == "remocao_produto":
                estoque.produtos[operacao["nome"]] = operacao["quantidade"]
                print(f"Remoção do produto '{operacao['nome']}' desfeita.")
            
# elif tipo == "venda":

    elif opcao == '0': #Sair
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")
