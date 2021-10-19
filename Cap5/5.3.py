"""
Se requiere un algoritmo para obtener un vector (C) de N elementos que
contenga la suma de los elementos correspondientes de otros dos vectores
(A y B). Represéntelo mediante el diagrama de flujo, el pseudocódigo
y el diagrama N/S.
I Contador y subíndice Entero
A, B, C Nombre de los vectores Real
N Número de elementos de cada arreglo Entero
"""
n = int(input("n:"))
a = []
b = []
c = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
# print(a)
# print(b)
for j in range(n):
    su = a[j] + b[j]
    c.append(su)
# print(c)
for k in range(n):
    print(c[k], end=' ')
