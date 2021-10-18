m, n = (map(int, input().split()))
matriz = []
for i in range(m):
    lista = list(map(int, input().split()))
    lista.reverse()
    matriz.append(lista)

for i in range(m):
    for j in range(n):
        print(matriz[i][j], end=' ')
    print()
