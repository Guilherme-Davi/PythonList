# Desenvolva uma função que receba uma lista de números e retorne o menor número encontrado nela.
numeros = [1,2,3,4,5,6,8,0,9,10,13,14,15]

def retorna_menor_numero(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    print(menor)

retorna_menor_numero(numeros)