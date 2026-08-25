from modulos.recursos import (limpar_terminal,ler_texto_obrigatorio,mostrar_menu,cadastrar_pedido,listar_pedidos,listar_clientes,buscar_cliente,remover_cliente)
from modulos.estoque import Estoque
from modulos.clientes import Clientes

estoque = Estoque()
clientes = Clientes()

while True:
    limpar_terminal()
    opcao = mostrar_menu()

    if opcao == '1': #Cadastrar cliente
        nome = ler_texto_obrigatorio("Digite o nome do cliente: ")  
        clientes.cadastrar(nome)
        print(f"Cliente cadastrado com sucesso: "f"{nome}")

    elif opcao == '2': #Listar clientes
        print("Clientes cadastrados:")
        clientes.listar_clientes()

    elif opcao == '3': #Buscar cliente
        codigo = int(ler_texto_obrigatorio("Digite o código do cliente: "))
        cliente = clientes.buscar_cliente(codigo)
        if cliente:
            print(f"Cliente encontrado: {cliente.nome}")
        else:
            print("Cliente não encontrado.")

    elif opcao == '4': #Remover cliente
        codigo = int(ler_texto_obrigatorio("Digite o código do cliente: "))
        clientes.remover_cliente(codigo)
        print("Cliente removido com sucesso.")

    elif opcao == '5': #Cadastrar produto
        nome = ler_texto_obrigatorio("Digite o nome do produto: ")
        preco = float(ler_texto_obrigatorio("Digite o preço do produto: "))
        quantidade = int(ler_texto_obrigatorio("Digite a quantidade do produto: "))
        estoque.cadastrar_produto(nome, preco, quantidade)
        print(f"Produto cadastrado com sucesso: {nome} - Preço: {preco} - Quantidade: {quantidade}")

    elif opcao == '6': #Listar produtos
        print("Estoque atual:")
        estoque.listar_produtos()

    elif opcao == '7': #Buscar produto
        codigo = int(ler_texto_obrigatorio("Digite o código do produto: "))
        produto = estoque.buscar_produto(codigo)
        if produto:
            print(f"Produto encontrado: {produto.nome} - Preço: {produto.preco} - Quantidade: {produto.quantidade}")
        else:
            print("Produto não encontrado.")

    elif opcao == '8': #Atualizar estoque
        codigo = int(ler_texto_obrigatorio("Digite o código do produto: "))
        nova_quantidade = int(ler_texto_obrigatorio("Digite a nova quantidade: "))
        estoque.atualizar_estoque(codigo, nova_quantidade)
        print("Estoque atualizado com sucesso.")

    elif opcao == '9': #Remover produto
        codigo = int(ler_texto_obrigatorio("Digite o código do produto: "))
        estoque.remover_produto(codigo)
        print("Produto removido com sucesso.")

    elif opcao == '10': #Listar produtos em ordem inversa
        print("Produtos em ordem inversa:")
        produtos_inverso = estoque.listar_produtos_inverso()
        for produto in produtos_inverso:
            print(f"ID: {produto.codigo} | Nome: {produto.nome} | Preço: {produto.preco} | Quantidade: {produto.quantidade}")

    elif opcao == '11': #Listar produtos ordenados por ID
        print("Produtos ordenados por ID:")
        produtos_ordenados = estoque.listar_produtos_ordenados_por_id()
        for produto in produtos_ordenados:
            print(f"ID: {produto.codigo} | Nome: {produto.nome} | Preço: {produto.preco} | Quantidade: {produto.quantidade}")

    elif opcao == '12': #Buscar produto por ID usando Busca Binaria
        codigo = int(ler_texto_obrigatorio("Digite o código do produto: "))
        produto = estoque.buscar_produto_binario(codigo)
        if produto:
            print(f"Produto encontrado: {produto.nome} - Preço: {produto.preco} - Quantidade: {produto.quantidade}")
        else:
            print("Produto não encontrado.")

    elif opcao == '13': #Realizar venda
        codigo_cliente = int(ler_texto_obrigatorio("Digite o código do cliente: "))
        codigo_produto = int(ler_texto_obrigatorio("Digite o código do produto: "))
        quantidade = int(ler_texto_obrigatorio("Digite a quantidade: "))
        estoque.realizar_venda_exemplo(codigo_cliente, codigo_produto, quantidade)
        print("Venda realizada com sucesso.")

    elif opcao == '14': #Listar vendas
        print("Fila de vendas:")
        vendas = estoque.listar_vendas()
        for venda in vendas:
            print(f"Cliente: {venda['cliente'].nome} | Produto: {venda['produto'].nome} | Quantidade: {venda['quantidade']}")

    elif opcao == '15': #Cadastrar pedido
            cadastrar_pedido(clientes, estoque)

    elif opcao == '16': #Listar pedidos
        listar_pedidos(clientes)

    elif opcao == '17': #Listar clientes com pedidos
        listar_clientes(clientes)

    elif opcao == '18': #Buscar cliente com pedidos
        buscar_cliente(clientes)

    elif opcao == '19': #Remover cliente com pedidos
        remover_cliente(clientes)

    elif opcao == '20': #Exibit produto mais vendido
        produto_mais_vendido = estoque.produto_mais_vendido()
        if produto_mais_vendido:
            print(f"Produto mais vendido: {produto_mais_vendido.nome} - Quantidade vendida: {produto_mais_vendido.quantidade_vendida}")
        else:
            print("Nenhum produto vendido ainda.")

    elif opcao == '21':  #Desfazer ultima operacao

    elif opcao == '0': #Sair
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")
