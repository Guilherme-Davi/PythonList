# Desenvolva uma função que receba uma lista e um valor.
# A função deve contar quantas vezes esse valor aparece na lista e retornar o total.
numeros = [1,2,3,3,4,5,6,8,9,10,13,14,15]

def contar_ocorrencias(lista, valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador += 1
    print(contador)

contar_ocorrencias(numeros, 3)