listaNumeros = []
while True:
    numero = int(input())
    if numero == 0:
        break
    else:
        listaNumeros.append(numero)
for num in listaNumeros:
    suma = 0
    for i in range(1, num+1):
        suma = suma + i
    print(suma)
