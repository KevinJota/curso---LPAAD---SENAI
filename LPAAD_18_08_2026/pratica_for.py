# FINALMENTE UTILIZAMOS FOR

tempos = [32,48,27,55,41,29]
atraso = 0 # contador
soma = 0 # acumulador

# ITERANDO pela lista e exibindo seus dados c/ FOR
for t in range(len(tempos)):
    print(f'entrega Nº {t+1}')
    print(f'tempo da entrega {tempos[t]} minutos')
    soma += tempos[t] 

    # classificando a ENTREGA
    if tempos[t] > 40:
        print("Status de entrega: ATRASADO")
        atraso+=1
    else:
        print('Status de entrega: Normal')
    print('***'*5)

# calculos finais
media = soma / len(tempos)
porcentagem = ( atraso / len(tempos)) * 100

# exibind registros gerais
print(f'tempo total das entregas: {soma} minutos')
print(f'tempo médio das entregas: {media} minutos')
print(f'Quantidade de entregas atrasadas: {atraso}')
print(f'porcentagem de entregas atrasadas: {porcentagem}%')

