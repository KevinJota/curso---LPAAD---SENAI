# criando uma calculadora_simples  que peça 2 números e execute um cáculo, utilizando apenas os recursos mencionados nesta aula

print("seja bem vindo á calculadora!")
print("insira 2 valores númericos a serem utilizados")
print("a calculadora irá executar todas as operações aritméticas com os valores inseridos")
n1 = float(input("digite o 1° valor:\n "))
n2 = float(input("digite o 2° valor:\n "))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
divisao = n1 / n2
div_inteira = n1 // n2
div_resto = n1 % n2
potencia = n1 ** n2
raiz_q = n1 ** (1/2)


print(f"adição: {soma}")
print(f"subtração: {sub}")
print(f"multiplicação: {mult}")
print(f"divisão: {divisao}")
print(f"divisão inteira: {div_inteira}")
print(f"resto de divisão: {div_resto}")
print(f"potência: {potencia}")


