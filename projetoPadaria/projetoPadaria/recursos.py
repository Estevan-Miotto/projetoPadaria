import os

def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto: 
            return texto
        print("Este campo é obrigatório.")

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

