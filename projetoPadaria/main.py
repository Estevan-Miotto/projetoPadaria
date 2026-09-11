
from modulos.operacoes.clientes import cadastrar_cliente, listar_clientes, buscar_cliente, remover_cliente

from modulos.operacoes.produtos import (
    cadastrar_produto,
    listar_produtos,
    buscar_produto,
    atualizar_estoque,
    remover_produto,
    listar_produtos_inverso,
    listar_produtos_ordenados_por_id,
    buscar_produto_binario,
    realizar_venda,
    listar_vendas,
    primeira_venda,
    valor_total_estoque,
    valor_total_vendas,
    clientes_e_valores_totais_gastos,
    cliente_que_mais_gastou,
    produto_mais_vendido
)

from modulos.services.estoque_service import EstoqueService

from modulos.recursos import limpar_terminal, mostrar_menu

service = EstoqueService()
clientes = service.clientes
produtos = service.produtos

while True:
    limpar_terminal()
    opcao = mostrar_menu()

    if opcao == "1":#Cadastrar clientes
        cadastrar_cliente(service)

    elif opcao == "2":#Listar clientes
        listar_clientes(service)

    elif opcao == "3":#Buscar cliente
        buscar_cliente(service)

    elif opcao == "4":#Remover cliente
        remover_cliente(service)

    elif opcao == "5":#Cadastrar produtos
        cadastrar_produto(service)

    elif opcao == "6":#Listar produtos
        listar_produtos(service)

    elif opcao == "7":#Buscar produto
        buscar_produto(service)

    elif opcao == "8":#Atualizar estoque
        atualizar_estoque(service)

    elif opcao == "9":#Remover produto
        remover_produto(service)

    elif opcao == "10":#Listar produtos em ordem inversa
        listar_produtos_inverso(service)

    elif opcao == "11":#Listar produtos ordenados por ID
        listar_produtos_ordenados_por_id(service)

    elif opcao == "12":#Buscar produto em arquivo binário
        buscar_produto_binario(service)

    elif opcao == '13':#Realizar venda
        realizar_venda(service)

    elif opcao == '14':#Listar vendas
        listar_vendas(service)

    elif opcao == '15':#Mostrar primeira venda
        primeira_venda(service)

    elif opcao == '16':#Mostrar valor total do estoque
        valor_total_estoque(service)

    elif opcao == '17':#Mostrar valor total das vendas
        valor_total_vendas(service)

    elif opcao == '18':#Mostrar clientes e seus valores totais gastos
        clientes_e_valores_totais_gastos(service)

    elif opcao == '19':#Mostrar cliente que mais gastou
        cliente_que_mais_gastou(service)

    elif opcao == '20':#Mostrar produto mais vendido
        produto_mais_vendido(service)

    elif opcao == "21":#Desfazer última operação
        mensagem = service.desfazer_ultima_operacao()

        if mensagem:
            print(mensagem)
        else:
            print("Não há operações para desfazer.")
                

    elif opcao == '0': #Sair
        print("Saindo do programa...")
        break

    else:#Opção inválida
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")
