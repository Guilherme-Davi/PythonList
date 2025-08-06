# Crie uma função que receba uma lista de objetos (onde cada objeto tem um atributo 'nome')
# e retorne uma nova lista contendo apenas os nomes de cada objeto.
lista_obj = [
    {"nome": "Jorge", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Pircio", "idade": 43, "cidade": "Paripueira"},
    {"nome": "Ana Banana", "idade": 62, "cidade": "Maceió"},
]

for i in range(len(lista_obj)):
    print(lista_obj[i])

for i in range(len(lista_obj)):
    print(lista_obj[i]["nome"])