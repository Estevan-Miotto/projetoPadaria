from recursos import limpar_terminal, ler_texto_obrigatorio, cliente, menu, listar_produtos, cadastrar_cliente, listar_clientes, listar_produtos

clientes = []
pedidos = []


while True:
    limpar_terminal()
    opcao = menu()

    if opcao == '1':
        nome = ler_texto_obrigatorio("Digite o nome do cliente: ")
        ID = ler_texto_obrigatorio("Digite o ID do cliente: ")
        cliente = cadastrar_cliente(nome, ID)
        clientes.append(cliente)
        print(f"Cliente cadastrado com sucesso: {cliente}")

    elif opcao == '2':
    
        clientes = listar_clientes(clientes)
        print("Clientes cadastrados:")
   
    elif opcao == '3':
        print(f"Pedido cadastrado com sucesso: {pedido}")

    elif opcao == '4':
        pedidos = listar_produtos()
        print("Produtos cadastrados:")
        for pedido in pedidos:
            print(pedido)

    elif opcao == '5':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")