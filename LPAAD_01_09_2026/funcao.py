# hoje(01/09/2026) o tema será FUNÇÕES

# parametro é um valor pré definido exigido na execução de alguma formula
# ARGUMENTO é o valor repassado que será usado para preencher o PARAMETRO
# enfim:
# PARAMETRO: VARIAVEL DECLARADA AO DEFINIR FUNÇÃO
# ARGUMENTO É O DADO ENVIADO QUANDO CHAMA A FUNÇÃO

# def calcular_media(PARAMETRO):
#     media = sum(PARAMETRO) / len(PARAMETRO)
#     return media

# UMA FUNÇÃO FOI CRIADA, agora para utiliza-la, basta chama-la pelo seu nome+(argument0)
# calcular_media(argumento)

# print X return
# PRINT exibe tal informação ou devolve resultado
# RETURN basicamente retorna um valor que poderá ser usado posteriormente em outra funções ou afins do programa


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# FUNCOES NATIVAS
# sorted() - RETORNA OS VALORES DE MANEIRA ORDENADA, DE MODO CRESCENTE aparentemente
# abs () - retorna a distancia/intervalo entre algum número até ZERO.
# round(numero, qtd de decimais) - arrendoda o valor para quantidade de casa decimais informada
# pow(numero, qtd de vezes a dar potencia) - calcula potencia


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# COLORINDO PRINT, PAI AMADO...
# nomenclatura gigantesca apenas para colorir o texto
# print(f'\033[31m 51 é pinga \033[107m')

# função feita para escolher a cor entre as opções e texto a ser colorido
def texto_colorido( texto , cor, estilo):

    if cor =='ciano':
        codigo = 36
        # print(f'\033[36m {a} \033[0m')
    elif cor == 'vermelho':
        codigo = 31
        #  print(f'\033[31m {a} \033[0m')
    else:
        codigo = 0

    if estilo == "negrito":
        formato = 1
    elif estilo == "italico":
        formato = 3
    else:
        formato = 0
    print(f'\033[\{formato}m;\{codigo}m {texto} [0m')
    

    
    return texto_colorido;

texto_colorido('aaaaaa', 'vermelho', 'negrito') 


