# Crie uma função que receba uma lista de números e retorne a soma de todos os seus valores.
numeros = [1,2,3,4,5,6,8,9,10,13,14,15]

def somar_valores(lista):
    i = 0
    for numero in lista:
        i += numero
    print(f'A soma dos valores da lista é: {i}')

somar_valores(numeros)