# OLA WHILE

producoes = []
meta_count = 0 # contador
total = 0 # acumulador


# primeiro loop para adicionar valores a lista selecionados pelo usuario
while True:
    valor = int(input('\ndigite um valor entre 300 ~ 800 peças: '))
    if valor < 300 or valor > 800:
        print('digite um valor aceitável ENTRE 300 E 800..\n')
        continue # recapitulando: continue ignora todo o Resto do loop e retorna para o inicio( BASICAMENTE REINICIA O LOOP, ele não finaliza o LOOP)

    # adicionado o valor na lista producoes
    print('O valor foi inserido na produção!')
    producoes.append(valor) # append adicionar valor na lista

    # perguntado se o programa deve continuar ou parar(encerrar loop WHILE)
    res = input('deseja continuar? clique ENTER, caso deseje PARAR, digite qualquer coisa: ')
    if res != "":
        print('PROGRAMA FINALIZADO\n')
        break # ENCERRA O LOOP(WHILE)

# segundo loop verificando os valores da lista e classificando seus valores
for a in range(len(producoes)):
    total += producoes[a]

    print(f"Resultado do {a+1}º TURNO: {producoes[a]} peças ")
    if producoes[a] >= 500:
        print("classificação: META ATINGIDA!\n")
        meta_count += 1

    elif producoes[a] >= 400 and producoes[a] < 500:
        print("classificação: ABAIXO DA META!\n")
    else:
        print("classificação: CRITÍCO!\n")


# calculos finais
n_turnos = len(producoes)
media = total / n_turnos
percent_meta = (meta_count / n_turnos) * 100

# registros finais
print(f' \nQuantidade de Turnos registrados: {n_turnos} turnos')
print(f' Quantidade de Turnos que atingiram a META: {meta_count} turnos')
print(f' Produção média de peças por turno: {media}')
print(f' Quantidade Total de Peças produzidas; {total}')
print(f' Percentual de Turnos que atingiram a META: {percent_meta}%')