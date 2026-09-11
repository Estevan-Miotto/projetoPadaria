from modulos.recursos import ler_texto_obrigatorio, ler_float, ler_inteiro
from modulos.estruturas.busca_binaria import busca_binaria

def cadastrar_produto(service):
    nome = ler_texto_obrigatorio("Digite o nome do produto: ")
    preco = ler_float("Digite o preço do produto: ")
    quantidade = ler_inteiro("Digite a quantidade em estoque: ")

    novo_produto = service.cadastrar_produto(nome, preco, quantidade)

    print(f"Produto cadastrado com sucesso: {novo_produto.nome} - Código: {novo_produto.codigo}")

def listar_produtos(service):
    produtos = service.listar_produtos()

    print("Lista de produtos:")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R$ {produto.preco:.2f} | Quantidade: {produto.quantidade}")

def buscar_produto(service):
    try:
        codigo = ler_inteiro("Digite o código do produto: ")
        produto = service.buscar_produto(codigo)

        if produto:
            print(f"Produto encontrado: {produto.nome}")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Digite apenas números.")

def atualizar_estoque(service):

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

def remover_produto(service):
    try:
        codigo = ler_inteiro("Digite o código do produto: ")
        produto = service.remover_produto(codigo)

        if produto:
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

def buscar_produto_binario(service):
    try:
        codigo = ler_inteiro("Digite o código do produto: ")
        produtos = service.listar_produtos()
        produtos_ordenados = sorted(produtos, key=lambda produto: produto.codigo)
        produto = busca_binaria(produtos_ordenados, codigo)

        if produto:
            print(f"Produto encontrado: {produto.nome}")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Digite apenas números.")

def realizar_venda(service):
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

def listar_vendas(service):
    vendas = service.listar_vendas()

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    print("Fila de vendas:")

    for venda in vendas:
        print(f"Código da venda: {venda.codigo} | Cliente: {venda.codigo_cliente} | Valor total: R$ {venda.valor_total:.2f}")

def primeira_venda(service):
    venda = service.primeira_venda()

    if venda:
        print(venda)
    else:
        print("Não há vendas na fila.")

def valor_total_estoque(service):
    total = service.valor_total_estoque()
    print(f"Valor total do estoque: R$ {total:.2f}")

def valor_total_vendas(service):
    total = service.valor_total_vendas()
    print(f"Valor total das vendas: R$ {total:.2f}")

def clientes_e_valores_totais_gastos(service):
    totais = service.clientes_e_valores_totais_gastos()

    print("Clientes e valores totais gastos:")

    if len(totais) == 0:
        print("Nenhuma venda registrada!!")
        return

    for item in totais:
        print(f"Cliente: {item['nome']} | Total gasto: R$ {item['total_gasto']:.2f}")

def cliente_que_mais_gastou(service):
    maior = service.cliente_que_mais_gastou()

    if maior is None:
        print("Nenhuma venda registrada ainda.")
    else:
        print(f"Cliente que mais gastou: {maior['nome']} - Total: R$ {maior['total_gasto']:.2f}")

def produto_mais_vendido(service):
    produto = service.produto_mais_vendido()

    if produto:
        print(f"Produto mais vendido: {produto.nome} - Quantidade vendida: {produto.quantidade_vendida}")
    else:
        print("Nenhum produto vendido ainda.")


























