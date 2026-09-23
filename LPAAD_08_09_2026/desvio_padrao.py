#  DESVIO PADRÃO: É UMA MEDIDA DE DISPERSÃO QUE DEMONSTRA O QUANTO OS VALORES
# SE AFASTAM DA MÉDIA
import math

tempos = [12,18,15,21,14,16]

# BASICAMENTE: VARIANCIA AO QUADRADO.
def calcular_desvio_padrao(lista):
    variancia = calcular_variancia(lista)
    desvio = math.sqrt(variancia)
    return desvio

# ---------------------------------------

# def calcular_variancia(lista):
#     media =  sum(lista) / len(lista)
#     soma = 0
#     for i in lista:
#         diferenca = i - media
#         soma += pow(diferenca, 2)
    
#     variancia = soma / len(lista)
#     return variancia

resultado = calcular_desvio_padrao(tempos)
print(f'desvui padrão: {resultado:.2f}')



