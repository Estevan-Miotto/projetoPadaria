def busca_binaria(produtos, codigo):
    inicio = 0
    fim = len(produtos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if produtos[meio].codigo == codigo:
            return produtos[meio]

        if produtos[meio].codigo < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None