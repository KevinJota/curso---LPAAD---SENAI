# iterando listas dentro de listas com FOR








vendas = [
     [3,4,5],
     [56,99,77],
     [55,66,11]
     ]

for linha in range(len(vendas)):
    for coluna in range(len(vendas[linha])):
        print(f'{vendas[linha][coluna]}')

    