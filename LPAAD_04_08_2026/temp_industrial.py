# um programa que monitore a temperatura industrial de uma fábrica em diferentes horários
# colinha: CTRL + D para alterae várias cédulas iguais ao mesmo tempo
#  precisa calcular a temperatura média da maquina
#  exiba manualmente(ou não) a temperatura maxima e minima registrada
# calcule a amplitude térmica(máxima - minima)

temp_min = min(72.3, 73.1,74.0,72.8,71.5,75.2,73.6,74.4)
temp_max = max(72.3, 73.1,74.0,72.8,71.5,75.2,73.6,74.4)

soma = 72.3+73.1+74.0+72.8+71.5+75.2+73.6+74.4
temp_media = soma / 8
amplitude = temp_max - temp_min

print(f"minima: {temp_min} °C")
print(f"máxima: {temp_max} °C")

print(f"temperatura média: {temp_media} °C")
print(f" A amplitude possui a diferença de {amplitude} °C")
