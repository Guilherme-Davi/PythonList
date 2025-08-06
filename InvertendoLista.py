# Escreva uma função que receba uma lista e retorne uma nova lista com os elementos na ordem inversa.
numeros = [1,2,3,4,5,6,8,9,10,13,14,15]

def inverter_lista(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    print(lista_invertida)

inverter_lista(numeros)