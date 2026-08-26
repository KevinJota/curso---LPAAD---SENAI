atendimento = [[120,135,128,141],[98,105,110,103],[150,145,160,155],[116,161,108,121]]
low_lista = []

low_atendimento = 0
maior_atendimento_semanal = atendimento[0][0]
maior_uni = 0
maior_atendimento_total = 0


# primeiro for para iterar as listas
for uni in range(len(atendimento)):

    # autoexplicativo
    print(f'\n{uni+1} UNIDADE:')
    total = sum(atendimento[uni])
    print(f'{total} atendimentos total')

# segundo FOR para iterar os ELEMENTOS de cada LISTA iterada pelo primeiro FOR
    for s in range(len(atendimento[uni])):
        print(f'atendimentos na semana {s+1}: {atendimento[uni][s]}')

        #  verifica se os atendimentos semanais de cada unidade se ela está abaixo de 110 e registra contagem 
        if atendimento[uni][s] < 110:
            low_atendimento+=1
            low_lista.append([uni+1, atendimento[uni][s]])

            
        # aqui verifica se a semana atual no loop possui mais atendimentos que o maior_atendimento_semanal, se sim, ele é substituido
        if atendimento[uni][s] > maior_atendimento_semanal:
            maior_atendimento_semanal = atendimento[uni][s]

# aqui registra o Nº Unidade e seu total caso ele seja o maior
    if total > maior_atendimento_total:
        maior_uni = uni + 1
        maior_atendimento_total = total



print(f'\nmaior atendimento semanal registrado: {maior_atendimento_semanal}')
print(f'A Unidade {maior_uni}º registrou {maior_atendimento_total} atendimentos no período.')
print(f'Obtivemos {low_atendimento} semanas abaixo de 110 atendimentos\n')
print(f'Semanas abaixo da meta e suas respectivas Unidades:\n')
# print(low_lista)
for a in range(len(low_lista)):
    print(f'Unidade: {low_lista[a][0]}º')
    print(f'{low_lista[a][1]} atendimentos')
    

        
