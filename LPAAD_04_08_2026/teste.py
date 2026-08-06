


# # mensagem de boas vindas simples..
# print('Seja Bem-vindo ao curso LPAAD')


# print("///"*7)
# # criando variaveis e atribuindo valores as mesmas..
# nome = "Kevin"
# idade = 22
# curso = "Inteligência e análise de dados"
# instituicao = "SENAI"
# profissão = "Estudante"


# # operadores aritemticos recorrentes:

# # operador / descrição / resultado
# #    +     /  adição   /  soma
# #    -     /  subtração   /  diferença
# #    *     /  multiplicação   /  produto
# #    /     /  divisão   /  Quociente
# #    %     /  resto de divisão   /  
# #    //     /  divisão inteira   /  Quociente
# #    **     /  potência   /  

# # Ordem de precedencia

# # Quando uma expressão possui mais de um operador, o Python segue uma ordem para realzar os calculos.

# # 1º   ()
# # 2º   **
# # 3º   *,/,//,%
# # 4º   +,-

# # exemplo

# res = 5 * 2 + 2 * (2**4 - 4) / 2
# print(res)

# print("///"*7)

# # hora de pedir alguma coisa pro usuario(INPUT)
# name = input("Digite seu nome: ")

# print("eai meu mano ", name ,"seja bem-vindo!")


# print('///'*7)

# # descobrindo o tipo de uma variavel

# # para verificar o tipo da variavel é ideal usar type(). exemplo:

# print(type(name))
# print(type(idade))


# # OBS: em Input(), caso não seja definido o tipo dele, o valor será definido como str(STRING) por padrão
# nota = floay(input('digite uma nota decimal de prova(ex: 9.6 , 6.5): '))
# estados = int(input('digite o número de estados que existem no Brasil(chuta um numero ai): '))
# nome_estado = str(input('digite o nome algum estado brasileiro: '))


# print(type(nota))
# print(type(estados))
# print(type(nome_estado))

# print('///'*7)



#   caracteres especiais:

# \n Quebra de linha
# \t Tabulação
# \" aspas dentro de texto
# \\ barra invertida


print("linha 1 \n Linha 2")

salario = float(input("digite o seu salário atual: "))

novo_salario = salario * 1.15

print(novo_salario)

nota = 7.56789

print('///'*7)

# formatando numreros floats
print(nota)
print(f"Nota formatada: {nota:.3f}") #7.567
print(f"Nota formatada: {nota:.2f}") #7.56
print(f"Nota formatada: {nota:.1f}") #7.5
print(f"Nota formatada: {nota:.0f}") #7