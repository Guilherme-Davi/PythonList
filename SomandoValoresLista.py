# Crie uma função que receba uma lista de números e retorne a soma de todos os seus valores.
numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def somar_valores(lista):
    i = 0
    for numero in lista:
        i += numero
    print(f'A soma dos valores da lista é: {i}')

somar_valores(numeros)