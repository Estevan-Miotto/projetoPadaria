from modulos.recursos import ler_texto_obrigatorio
from modulos.models.cliente import Cliente


def cadastrar_cliente(clientes, persistencia):
    nome = ler_texto_obrigatorio("Digite o nome do cliente: ")

    if clientes:
        proximo_codigo = max(cliente.codigo for cliente in clientes) + 1
    else:
        proximo_codigo = 1

    novo_cliente = Cliente(proximo_codigo, nome)

    clientes.append(novo_cliente)

    persistencia.salvar_clientes(clientes)

    print(f"Cliente cadastrado com sucesso: "f"{novo_cliente.nome} - "f"Código: {novo_cliente.codigo}")

def listar_clientes(clientes):
    print("Lista de clientes:")

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"Código: {cliente.codigo} | "f"Nome: {cliente.nome}")

def buscar_cliente(clientes):
    try:
        codigo = int(
            ler_texto_obrigatorio("Digite o código do cliente: ")
        )

        for cliente in clientes:
            if cliente.codigo == codigo:
                print(f"Cliente encontrado: "f"{cliente.nome}")
                return

        print("Cliente não encontrado.")

    except ValueError:
        print("Digite apenas números.")

def remover_cliente(clientes, persistencia):
    try:
        codigo = int(
            ler_texto_obrigatorio(
                "Digite o código do cliente: "
            )
        )

        for cliente in clientes:
            if cliente.codigo == codigo:
                clientes.remove(cliente)
                persistencia.salvar_clientes(clientes)

                print(
                    f"Cliente {cliente.nome} removido com sucesso."
                )
                return

        print("Cliente não encontrado.")

    except ValueError:
        print("Digite apenas números.")


