
# LISTA COM DICIONARIOS
produtos = [
    {
        'produto': 'Notebook',
        'preço': 4200,
        'estoque': 8
    },
    {
        'produto': 'Mouse',
        'preço': 120,
        'estoque': 25
    },
    {
        'produto': 'Monitor',
        'preço': 1350,
        'estoque': 4
    },
    {
        'produto': 'Teclado',
        'preço': 280,
        'estoque': 15
    },
    {
        'produto': 'Headset',
        'preço': 450,
        'estoque': 3
    }
]

count = 0
lista = []

# iterando normal com FOR pelos 4 dicionarios na LISTA:
for produto in produtos:
    print(f'produto: {produto['produto']} - {produto['estoque']} : unidades - preço: {produto['preço']}')

    # verificando quais produtos possuem estoque abaixo de 10 unidades
    if produto['estoque'] < 10:
        #  adiciona o dicionario do produto á uma lista separadamente e faz contagem
        lista.append(produto)
        count+=1


# exibindo resultados finais



print(f'\nNúmero de Produtos com baixo estoque(abaixo de 10 unidades): {count}')

# outro FOR para exibir os produtos captados pela LISTA que pegou produtos com baixo ESTOQUE
print('produtos que precisam de reposição: ')
for produto in lista:
    print(f'produto: {produto['produto']} - {produto['estoque']} : unidades')


    





