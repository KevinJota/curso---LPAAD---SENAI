# primeiro quartial
# N representa o NUMERO DE OBJETOS
# PQ1 = ( N + 1) / 4 

# Segundo quartil
# PQ2 = ( N + 1) / (4 / 2)

# Terceiro Quartil
# PQ3 =  (3 * (N + 1)) / 4


def calcular_valor_quartil(dados, posicao):
    posicao_inteira = int(posicao)
    if posicao == posicao_inteira:
        return dados[posicao_inteira - 1]
    
    parte_decimal = posicao - posicao_inteira
    valor_inferior = dados[posicao_inteira - 1]
    valor_superior = dados[posicao_inteira]

    diferenca = valor_superior - valor_inferior
    acrescimo = diferenca * parte_decimal

    return valor_inferior + acrescimo

vendas = [42,18,35,27,50,31,22]


def calcula_quartil(lista):
    dados = sorted(lista)
    valor = len(dados)
    PQ1_completo = (valor + 1) / 4 # para pegar a posição completa
    PQ2_completo = (valor + 1) / (4 / 2) # para pegar a posição completa
    PQ3_completo = (3 * (valor / 1)) / 4 # para pegar a posição completa

    q1 = calcular_valor_quartil(dados, PQ1_completo)
    q2 = calcular_valor_quartil(dados, PQ2_completo)
    q3 = calcular_valor_quartil(dados, PQ3_completo)
    return q1, q2, q3

q1, q2, q3 = calcula_quartil(vendas)

print('---'*15)

print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')

print('---'*15)


