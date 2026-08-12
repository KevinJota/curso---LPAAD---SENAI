# Recapitulando LISTAS em python
# array/algo que permite armazenar vários valores numa unica variavel

# lista de vendas
vendas = [340,200,400,200,400]


# LISTA.APPEND() PARA ADICONAR COISAS NA LISTA
# registra novas vendas/valores da lista
vendas.append(int(input('digite os ganhos de 2º feira: ')))
# vendas.append(float(input('digite os ganhos de 3º feira: ')))
# vendas.append(float(input('digite os ganhos de 4º feira: ')))
# vendas.append(float(input('digite os ganhos de 5º feira: ')))

# exibindp
print(vendas)

#identifica o Nº registros na lista
qtd = len(vendas)
print(f' quantidade de registros: {qtd}')
menor = min(vendas)
maior = max(vendas)
print(f' maior venda: {maior} /// menor venda: {menor}')

# acessando dados da lista pelo indice
print(vendas[0])
print(vendas[2])