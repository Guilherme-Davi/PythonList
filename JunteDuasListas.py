# Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas.
natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def junte_duas_listas(lista1, lista2):
    lista3 = lista1 + lista2
    lista3.sort()  # Ordena a lista resultante
    print(lista3)

junte_duas_listas(natureza, tecnologia)