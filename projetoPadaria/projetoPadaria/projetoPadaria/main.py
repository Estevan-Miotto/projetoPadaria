from recursos import (limpar_terminal,ler_texto_obrigatorio,menu,cadastrar_pedido,listar_pedidos,listar_clientes)
from estoque import Estoque
from Clientes import Clientes

estoque = Estoque()
clientes = Clientes()

while True:
    limpar_terminal()
    opcao = menu()

    if opcao == '1':
        nome = ler_texto_obrigatorio("Digite o nome do cliente: ")  
        clientes.cadastrar(nome)
        print(f"Cliente cadastrado com sucesso: "f"{nome}")

    elif opcao == '2':
        print("Clientes cadastrados:")
        clientes.listar_clientes()

    elif opcao == '3':
        print("Pedido cadastrado com sucesso.")

    elif opcao == '4':
        print("Estoque atual:")
        estoque.listar_produtos()

    elif opcao == '5':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")