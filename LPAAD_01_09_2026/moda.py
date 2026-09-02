lista = [12,15,18,15,20,15,17]

def calcula_unimodal(lista):
    moda_qtd = 0
    moda = 0
    for a in lista:
        valor = lista.count(a)
        print(f"O valor {a} apareceu {valor} vez(es)!")
        if valor > moda_qtd:
            moda = a
            moda_qtd = valor
    print(f'\nO elemento que mais apareceu foi "{moda}" registrado {moda_qtd} vez(es).')


# calcula_unimodal(lista)


listaA = [12,12,44,1,1,6,6,6,7]

def calcula_modal_geral(lista):
    modal_lista = []
    moda_qtd = 1
    for a in lista:
        valor = lista.count(a)
        if valor > moda_qtd:
            moda_qtd = valor
            modal_lista = [a]
        elif valor == moda_qtd and a not in modal_lista:
            modal_lista.append(a)

        print(f"O valor {a} apareceu {valor} vez(es)!")

    return modal_lista, moda_qtd




    

modas, moda_frequencia = calcula_modal_geral(listaA)
print(modas)
print(moda_frequencia)

