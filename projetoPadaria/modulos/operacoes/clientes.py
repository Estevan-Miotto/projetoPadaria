from modulos.recursos import ler_texto_obrigatorio
from modulos.models.cliente import Cliente


def cadastrar_cliente(service):
    nome = ler_texto_obrigatorio("Digite o nome do cliente: ")
    novo_cliente = service.cadastrar_cliente(nome)

    print(f"Cliente cadastrado com sucesso: {novo_cliente.nome} - Código: {novo_cliente.codigo}")


def listar_clientes(service):
    clientes = service.listar_clientes()

    print("Lista de clientes:")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"Código: {cliente.codigo} | Nome: {cliente.nome}")


def buscar_cliente(service):
    try:
        codigo = int(ler_texto_obrigatorio("Digite o código do cliente: "))
        cliente = service.buscar_cliente(codigo)

        if cliente:
            print(f"Cliente encontrado: {cliente.nome}")
        else:
            print("Cliente não encontrado.")

    except ValueError:
        print("Digite apenas números.")


def remover_cliente(service):
    try:
        codigo = int(ler_texto_obrigatorio("Digite o código do cliente: "))
        cliente = service.remover_cliente(codigo)

        if cliente:
            print(f"Cliente {cliente.nome} removido com sucesso.")
        else:
            print("Cliente não encontrado.")

    except ValueError:
        print("Digite apenas números.")


