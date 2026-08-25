import os,produtos

def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto: 
            return texto
        print("Este campo é obrigatório.")

def mostrar_menu():
    print("\n==============================")
    print("SISTEMA DE ESTOQUE E VENDAS")
    print("==============================")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Buscar cliente")
    print("4 - Remover cliente")
    print("5 - Cadastrar produto")
    print("6 - Listar produtos")
    print("7 - Buscar produto")
    print("8 - Atualizar estoque")
    print("9 - Remover produto")
    print("10 - Listar produtos em ordem inversa")
    print("11 - Listar produtos ordenados por ID")
    print("12 - Buscar produto por ID usando Busca Binaria")
    print("13 - Realizar venda simples de exemplo")
    print("14 - Visualizar fila de vendas")
    print("15 - Visualizar primeira venda da fila")
    print("16 - Exibir valor total do estoque")
    print("17 - Exibir valor total das vendas")
    print("18 - Exibir clientes e valores totais gastos")
    print("19 - Exibir cliente que mais gastou")
    print("20 - Exibir produto mais vendido")
    print("21 - Desfazer ultima operacao")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_pedido(produto, quantidade):
    return {'produto': produto, 'quantidade': quantidade}

def listar_pedidos():
    return [{"produtos":{"ovo": 100,"Pão": 50,"Leite": 20,"Farinha": 30,"Açúcar": 25}}]

def listar_clientes(self):
    for cliente in self.clientes.values():
        print(f"ID: {cliente.id} | "f"Nome: {cliente.nome}")

def buscar_cliente(self, codigo):
    pass

def remover_cliente(self, codigo):
    pass

