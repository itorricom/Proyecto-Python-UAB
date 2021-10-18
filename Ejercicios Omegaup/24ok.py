n = int(input())
matriz = []
for i in range(n):
    lista = []
    lista = list(map(int, input().split()))
    matriz.append(lista)
diagonal = 0
for i in range(n):
    for j in range(n):
        if [i] == [j]:
            diagonal = diagonal + matriz[i][j]
si = diagonal/n
if si == matriz[0][0]:
    print("SI")
else:
    print("NO")
