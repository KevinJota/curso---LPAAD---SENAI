# mediana - posição central entre os valores
# moda - o valor mais frequente entre valores
# média - soma e divisão entre a q Qunatidade total de valores

def calcular_mediana(aaa):

    lista = sorted(aaa)
    tamanho = len(aaa)
    print(lista)
    mediana = 0

    if tamanho % 2 == 0:
        print('conjunto é par')
        while len(aaa) != 2:
            aaa.remove(min(aaa))
            aaa.remove(max(aaa))
        mediana = (aaa[1] - aaa[0]) // 2 + aaa[0]
        # print(mediana)

    else:
        print('IMPAR')
        while len(aaa) != 1:
           aaa.remove(min(aaa))
           aaa.remove(max(aaa))    
        mediana = aaa[0]
        
    return mediana;

a = [23,14,31,17,20]
b = [21,40,60,77,88,10]

mediana = calcular_mediana(b)
print(f'essa é a mediana do conjunto: {mediana}')