# SEM UTILIZAR FOR / WHILE

# Situação: Uma indústria possui uma linha com capacidade planejada de 500 unidades por turno. Nos 
# últimos seis turnos, foram registradas as seguintes produções: 485, 510, 472, 498, 455 e 520 unidades. 
# A equipe utiliza a produção média para avaliar o desempenho geral do período, ver Tabela.
# Além da classificação geral, existe uma regra de segurança operacional: Se pelo menos um turno 
# apresentar produção inferior a 460 unidades, deverá ser emitido um alerta operacional, 
# independentemente da classificação obtida pela média.
# Desenvolva um programa que apresente:
# • armazene as produções em uma lista; 
# • determine a quantidade de turnos analisados; 
# • calcule a produção total do período; 
# • calcule a produção média por turno; 
# • identifique a maior e a menor produção registrada; 
# • classifique o desempenho geral do período; 
# • verifique se deve ser emitido um alerta operacional.

producao = []
valor_limite = 460

valor_producao1 = 485
producao.append(valor_producao1)

valor_producao2 = 510
producao.append(valor_producao2)

valor_producao3 = 472
producao.append(valor_producao3)

valor_producao4 = 498
producao.append(valor_producao4)

valor_producao5 = 455
producao.append(valor_producao5)

valor_producao6 = 520
producao.append(valor_producao6)


if valor_producao1 > valor_limite or valor_producao2 > valor_limite or valor_producao3 > valor_limite or valor_producao4 > valor_limite or valor_producao5 > valor_limite or valor_producao6 > valor_limite:
    print(f' produção de unidades está abaixo do limite minimo aceitavél de {valor_limite} unidades!')
    print(f'ALERTA OPERACIONAL FOI ACIONADO!')

# calculando
num_turnos = len(producao)
total_prod = sum(producao)
media_prod = total_prod / num_turnos
menor_prod = min(producao)
maior_prod = max(producao)
print('///'*7)

# dados gerais aqui
print(f'Turnos analisados: {num_turnos}')
print(f'produção total do periodo: {total_prod}')
print(f'produção média por turno {media_prod}')
print(f'menor produção registrada: {menor_prod}')
print(f'maior produção registrada: {maior_prod}\n')


# classificação geral do périodo:
print('DESEMPENHO GERAL DO PÉRIODO:')
if media_prod >= 500:
    print('META ATINGIDA')
elif media_prod >= 480 and media_prod <= 499.99:
    print('ATENÇÃO Á META')
else:
    print('ABAIXO DA META')


