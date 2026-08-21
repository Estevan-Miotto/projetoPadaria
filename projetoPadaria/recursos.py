import os

def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto: 
            return texto
        print("Este campo é obrigatório.")

def listar_clientes(clientes):
    for cliente in clientes:
        print(cliente)

def listar_produtos():
    # Aqui você pode adicionar a lógica para listar pedidos cadastrados
    return []

def cadastrar_cliente(nome, ID):
    cliente = {
        'nome': nome,
        'ID': ID,
    }
    # Aqui você pode adicionar a lógica para salvar o cliente em um banco de dados ou arquivo
    return cliente

def menu():
    print("=== Sistema de Padaria ===")
    print("1. Cadastrar Cliente")
    print("2. Listar Clientes")
    print("3. Cadastrar Pedido")
    print("4. Listar Pedidos")
    print("5. Sair")
    return input("Escolha uma opção: ")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_pedido(produto, quantidade):
    return {
        'produto': produto,
        'quantidade': quantidade
    }


def listar_pedidos():
    return []

def cliente(nome, ID):
    return {
        'nome': nome,
        'ID': ID,
    }


