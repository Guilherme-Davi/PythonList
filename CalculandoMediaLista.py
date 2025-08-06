# Crie uma função que receba uma lista de números e retorne a média aritmética desses valores.
numeros = [1,2,3,4,5,6,8,9,10,13,14,15]

def media_lista(lista):
    soma = sum(lista)
    media = soma / len(lista)
    print(media)

media_lista(numeros)