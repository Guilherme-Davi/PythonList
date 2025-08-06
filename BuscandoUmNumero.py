numeros = [1,2,3,4,5,6,8,9,10,13,14,15]

def encontrar_numero(lista, numero):
    for i in lista:
        if i == numero:
            return True
    else:
        return False
    
adivinha = int(input("Digite um número: "))
    
print(encontrar_numero(numeros, adivinha))