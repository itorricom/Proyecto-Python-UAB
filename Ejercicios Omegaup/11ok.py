"""
Dado un entero , determina la potencia a la que se eleva el 2 para llegar a N, es decir 2^k=N. Debes determinar k.
"""

n = int(input())
for k in range(1, n):
    if n == 2**k:
        break
print(k)
