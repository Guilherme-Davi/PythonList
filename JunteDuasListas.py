# Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas.
numeros1 = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
numeros2 = [1,2,3,4,5,6,8,9,10,13,14,15]

def junte_duas_listas(lista1, lista2):
    lista3 = lista1 + lista2
    lista3.sort()  # Ordena a lista resultante
    print(lista3)

junte_duas_listas(numeros1, numeros2)