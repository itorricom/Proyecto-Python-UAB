
n, m = (map(int, input().split()))
matrizA = []
for i in range(n):
    lista = list(map(int, input().split()))
    matrizA.append(lista)

matrizT = []
for x in range(0, n):
    lista = []
    for y in range(0, m):
        lista.append(matrizA[x][y])
    matrizT.append(lista)
for x in range(0, m):
    for y in range(0, n):
        print(matrizT[y][x], end=' ')
    print()
""" 
2 3
4 2 3
5 7 1 
"""
