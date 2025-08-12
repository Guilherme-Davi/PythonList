# Desenvolva uma função que receba uma lista e um valor.
# A função deve contar quantas vezes esse valor aparece na lista e retornar o total.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def contar_ocorrencias(lista, valor):
    contador = 0
    for i in lista:
        if i == valor:
            contador += 1
    print(contador)

contar_ocorrencias(numeros, 3)