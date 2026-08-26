
# lista com conjuntos de clientes definidos como dicionarios
clientes = [
    {
        "nome": "João",
        "idade": 30
    },
    {
        "nome": "Ana",
        "idade": 19
    },
    {
        "nome": "Yan",
        "idade": 38
    }
]

for cliente in clientes:
    print(cliente)

# # for percorre somente a chave 
# for chave in cliente:
#     print(f'{chave}')

# agora o FOR RODA CHAVE  e VALOR
# for chave, valor in  cliente.items():
#     print(f'{chave}: {valor}')

print('-'*25)

# exemplo:
produto = {
    'nome': 'Notebook',
    'valor': 4200,
    'estoque': 8
}


# itera somente as chaves
for a in  cliente.keys():
    print(f'{a}')

print('-'*25)

# itera somente os valores
for a in  cliente.values():
    print(f'{a}')

