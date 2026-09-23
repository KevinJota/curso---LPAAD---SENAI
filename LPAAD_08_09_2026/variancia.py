# como calcular variancia?
u = 0
lista = [12,18,15,21,14,16]

media =  sum(lista) // len(lista)
#média dá 16

# pow(numero, n_potencia)
def calcular_variancia(lista):
    media =  sum(lista) / len(lista)
    soma = 0
    for i in lista:
        diferenca = i - media
        soma += pow(diferenca, 2)
    
    variancia = soma / len(lista)
    return variancia
        
print(f'variancia da lista: {calcular_variancia(lista):.2f}')


# exemplo da lousa utlizando IDADE - IDADE MÉDIA >>> RESULTARA  em DIFERENCA logo>>> DIFERENCA SERÁ POTENCIA IGUAL AO QUADRADO(**2)  
diferenca = 22 - 25
variancia = pow(diferenca, 2) / 12
print(f'variancia idade: {variancia:.2f}')
