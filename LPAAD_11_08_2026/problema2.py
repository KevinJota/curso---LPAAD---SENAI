# SEM UTILIZAR FOR / WHILE

# Controle de Velocidade
# Situação: Um radar registrou a velocidade de um veículo em uma via cujo limite é de 70 km/h.
# Desenvolva um programa que:
# • Leia a velocidade do veículo; 
# • Verifique se ele ultrapassou 70 km/h; 
# • Informe se o veículo está dentro do limite ou se o motorista foi multado;
# • Calcule a multa considerando R$ 9,00 por km/h excedente;
# • Exiba o valor total da multa.
# • Calcule o percentual de excesso de velocidade em relação ao limite

velocidade = int(input('qual a velocidade registrada pelo radar? '))
limite_vel = 70


# verifica se velocidade do veiculo está acima do limite de 70KM/H 
if velocidade > limite_vel:
    print(f'Veiculo ultrapassou via acima do limite permitido de {limite_vel} Km/H. MULTADO!')

    vel_excesso = velocidade - limite_vel
    multa_aplicada = 9.00 * vel_excesso
    print(f'Velocidade registrada: {velocidade} Km/H')
    print(f'Multa aplicada: R$ {multa_aplicada}')

    percentual_excesso = ((velocidade - limite_vel) * 100) / limite_vel

    print(f'percentual de excesso de velocidade registrado: {percentual_excesso:.0f}%')

    if percentual_excesso >= 50:
        print('Velocidade excede 50% acima de do limite permitido!')
        print('Carteira de motorista SUSPENSA por 1 ANO!')


print('\nfim do programa, tenha um ótimo dia.')