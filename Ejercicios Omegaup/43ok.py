numero = int(input())
listaNumeros = []
while numero > 1:
    listaNumeros.append(numero)
    if numero % 2 == 0:
        numero = int(numero/2)
    else:
        numero = int((numero*3)+1)
listaNumeros.append(1)
listaNumeros.sort()
for num in listaNumeros:
    print(num, end=' ')
