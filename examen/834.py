numeros = 5
lista = []
for i in range(numeros):
    num = int(input())
    if num % 2 != 0:
        lista.append(num)
mayor = max(lista)
print(mayor)
