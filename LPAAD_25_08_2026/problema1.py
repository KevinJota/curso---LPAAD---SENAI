# percorrendo e classificando os elementos de uma lista simples

estoque = [18,5,0,32,4,7,0,14,3]


esgotado = 0
critico = 0

print(f'lista de produtos e sua situação\n')

for i in range(len(estoque)):

    print(f'PRODUTO {i+1}')
    if estoque[i] > 5:
        print(f'Estoque: {estoque[i]}')
        print('Situação: Disponivel!\n')

    elif estoque[i] > 1 and estoque[i] <=5:
            print(f'Estoque: {estoque[i]}')
            print('Situação: Critíco!\n')
            esgotado+=1

    else:
            print(f'Estoque: {estoque[i]}')
            print('Situação: ESGOTADO!\n')
            critico+=1

print(f'Quantidade de produtos ESGOTADOS: {esgotado}')
print(f'Quantidade de produtos em situação CRITÍCA: {critico}')

percentual = (esgotado + critico) * 100 / len(estoque)

print(f'percentual de produtos ESGOTADO ou CRITICO:  {percentual:.2f}%')
