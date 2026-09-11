Grupo:
1111500 - Rdrigo lordi carneiro dos santos
1139777 - Erick gadini mendonça
1137717 - João Victor Bordignon
1139560 - Estevan Miotto Bertosso 1139594 - Joao Rafael Dias Reis
1139424 - Gabriel Farezin Mello

# Projeto Padaria

Sistema de gerenciamento de estoque, clientes e vendas desenvolvido em Python como trabalho da disciplina **Organização e Abstração na Programação**.

## Objetivo

O projeto tem como objetivo aplicar conceitos de programação e estruturas de dados na criação de um sistema simples para gerenciamento de uma padaria.

O sistema permite:

- Cadastrar clientes
- Listar clientes
- Buscar clientes
- Remover clientes
- Cadastrar produtos
- Listar produtos
- Buscar produtos
- Atualizar estoque
- Remover produtos
- Listar produtos em ordem inversa
- Listar produtos ordenados por ID
- Buscar produtos utilizando busca binária
- Realizar vendas
- Visualizar a fila de vendas
- Visualizar a primeira venda da fila
- Calcular o valor total do estoque
- Calcular o valor total das vendas
- Consultar os valores gastos por cada cliente
- Identificar o cliente que mais gastou
- Identificar o produto mais vendido
- Desfazer a última operação

## Tecnologias utilizadas

- Python 3
- Arquivos CSV para persistência dos dados
- Programação orientada a objetos
- Estruturas de dados implementadas manualmente

## Estruturas de dados

O projeto utiliza diferentes estruturas de dados de acordo com a necessidade de cada operação.

### Lista Simplesmente Encadeada (LSE)

Utilizada para armazenar os clientes.

### Lista Duplamente Encadeada (LDE)

Utilizada para armazenar os produtos, permitindo também a listagem em ordem inversa.

### Fila

Utilizada para armazenar as vendas realizadas, seguindo o conceito FIFO
(First In, First Out).

### Pilha

Utilizada para armazenar o histórico das operações e possibilitar o recurso de desfazer a última operação, seguindo o conceito LIFO
(Last In, First Out).

### Busca Binária

Implementada para realizar buscas de produtos pelo código após a ordenação dos produtos por ID.

## Organização do projeto

```text
projetoPadaria/
│
├── main.py
│
└── modulos/
    │
    ├── data/
    │   ├── clientes.csv
    │   ├── produtos.csv
    │   └── vendas.csv
    │
    ├── estruturas/
    │   ├── dnodo.py
    │   ├── fila.py
    │   ├── lde.py
    │   ├── lse.py
    │   ├── nodo.py
    │   ├── pilha.py
    │   └── busca_binaria.py
    │
    ├── models/
    │   ├── cliente.py
    │   ├── produto.py
    │   └── venda.py
    │
    ├── services/
    │   ├── estoque_service.py
    │   └── persistencia_service.py
    │
    ├── operacoes/
    │   ├── clientes.py
    │   └── produtos.py
    │
    └── recursos.py