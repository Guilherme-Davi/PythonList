numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def encontrar_numero(lista, numero):
    for i in lista:
        if i == numero:
            return True
    else:
        return False
    
adivinha = int(input("Digite um número: "))
    
print(encontrar_numero(numeros, adivinha))