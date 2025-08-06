def encontrar_segundo_maior(lista):
    list = lista
    print(list)
    maior = list[0]
    for i in list:
        if i > maior:
            maior = i
    list.remove(maior)
    segundo = list[0]
    for i in list:
        if i > segundo:
            segundo = i
    print(f"O segundo maior número da lista é: {segundo}")

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

encontrar_segundo_maior(numeros)