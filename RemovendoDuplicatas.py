# Elabore uma função que receba uma lista com valores possivelmente duplicados e
# retorne uma nova lista contendo apenas os valores únicos, sem repetições.

numeros = [1,2,3,3,4,5,6,6,8,9,9,10,13,14,15]

def removendo_duplicatas(lista):
    list = []
    for i in lista:
        if i not in list:
            list.append(i)
    print(list)

removendo_duplicatas(numeros)