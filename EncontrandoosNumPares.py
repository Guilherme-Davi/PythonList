numeros = [1,2,3,4,5,6,8,9,10,13,14,15]
def encontrar_pares(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)

encontrar_pares(numeros)