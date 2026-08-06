
# desenvolver um programa que:

#  armazena a produção de cada dia em uma variavel
# calcule a produção total da semana
# calcule a media diaria
# determine quantas peças faltariam para atingir a meta semanal de 7.000 peças
# exiba todas as informações na tela

total = 0
meta = 7000

dia1 = int(input("quanto foi produzido no dia 1?"))
total += dia1

dia2 = int(input("quanto foi produzido no dia 2?"))
total += dia2

dia3 = int(input("quanto foi produzido no dia 3?"))
total += dia3

dia4 = int(input("quanto foi produzido no dia 4?"))
total += dia4

dia5 = int(input("quanto foi produzido no dia 5?"))
total += dia5

media = total // 5
resumo = meta - total 

print(f" a média diária desta semana foi de {media} peças")
print(f" a quantidade necessária para atingir a meta são de {resumo} peças!")
