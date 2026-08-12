# SEM UTILIZAR FOR / WHILE

# desempenho de uma rede de Supermercados


dia = ['Seg','Ter','Qua','Qui','Sex']
faturamento = [18500.00,21300.00,17800.00,24800.00,27400.00,]

num_dias = len(dia)
total_fat = sum(faturamento)
media_day = total_fat / num_dias

menor_fat = min(faturamento)
maior_fat = max(faturamento)

# aqui será utilizado listas com dados sobre uma unidade
# e apartir dela será exibido informações como:

print(f'Quantidade de Dias analisados: {num_dias}')
print(f'faturamento total da unidade: {total_fat}')
print(f'faturamento médio diário: {media_day}\n')
print(f'menor faturamento registrado: {menor_fat}')
print(f'maior faturamento registrado: {maior_fat}')



# após exibir os dados da unidade, aqui será feito uma avaliação sobre o Desempnho da unidade
# baseado no faturamento médio diário(media_day):

if media_day >= 22000:
    print(f'BOM DESEMPENHO')
elif media_day >= 19000 and media_day <= 21999:
    print(f'Desempenho Regular')
else:
    print(f'Desempenho critíco!')