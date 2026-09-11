from modulos.recursos import ler_texto_obrigatorio, ler_float, ler_inteiro
from modulos.models.produto import Produto
from modulos.estruturas.busca_binaria import busca_binaria

def cadastrar_produto(produtos, persistencia):

    nome = ler_texto_obrigatorio("Digite o nome do produto: ")

    preco = ler_float("Digite o preço do produto: ")

    quantidade = ler_inteiro("Digite a quantidade em estoque: ")

    if produtos:
        proximo_codigo = max(produto.codigo for produto in produtos) + 1
    else:
        proximo_codigo = 1

    novo_produto = Produto(proximo_codigo,nome,preco,quantidade)

    produtos.append(novo_produto)

    persistencia.salvar_produtos(produtos)

    print(f"Produto cadastrado com sucesso: "f"{novo_produto.nome} - "f"Código: {novo_produto.codigo}")

def listar_produtos(produtos):
    print("Lista de produtos:")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f} | Quantidade: {produto.quantidade}")

def buscar_produto(produtos):
    try:
        codigo = int(ler_texto_obrigatorio("Digite o código do produto: "))

        for produto in produtos:
            if produto.codigo == codigo:
                print(f"Produto encontrado: {produto.nome}")
                return

        print("Produto não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def atualizar_estoque(produtos, service):

    try:
        codigo = ler_inteiro("Digite o código do produto: ")
        nova_quantidade = ler_inteiro("Digite a nova quantidade: ")

        produto = service.atualizar_estoque(codigo, nova_quantidade)

        if produto:
            print(f"Estoque atualizado: {produto.nome} | Quantidade: {produto.quantidade}")
        else:
            print("Produto não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def remover_produto(produtos, persistencia):
    try:
        codigo = ler_inteiro("Digite o código do produto: ")

        produto = None

        for item in produtos:
            if item.codigo == codigo:
                produto = item
                break

        if produto:
            produtos.remove(produto)
            persistencia.salvar_produtos(produtos)
            print(f"Produto {produto.nome} removido com sucesso.")
        else:
            print("Produto não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def listar_produtos_inverso(service):
    produtos = service.listar_produtos_inverso()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("Produtos em ordem inversa:")

    for produto in produtos:
        print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f} | Quantidade: {produto.quantidade}")

def listar_produtos_ordenados_por_id(service):
    produtos = service.listar_produtos_ordenados_por_id()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("Produtos ordenados por ID:")

    for produto in produtos:
        print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f} | Quantidade: {produto.quantidade}")

def buscar_produto_binario(produtos):
    try:
        codigo = ler_inteiro("Digite o código do produto: ")

        produtos_ordenados = sorted(produtos, key=lambda produto: produto.codigo)
        produto = busca_binaria(produtos_ordenados, codigo)

        if produto:
            print(f"Produto encontrado: {produto.nome}")
        else:
            print("Produto não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def realizar_venda(produtos, service):
    try:
        codigo_cliente = ler_inteiro("Digite o código do cliente: ")
        codigo_produto = ler_inteiro("Digite o código do produto: ")
        quantidade = ler_inteiro("Digite a quantidade: ")

        venda = service.realizar_venda_exemplo(codigo_cliente, codigo_produto, quantidade)

        if venda:
            print("Venda realizada com sucesso.")
        else:
            print("Não foi possível realizar a venda.")
    except ValueError:
        print("Digite apenas números.")








































