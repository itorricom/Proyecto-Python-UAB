nroAlmunos = int(input())
notas = list(map(int, input().split()))
notas.sort()
notas.reverse()
for n in notas:
    print(n, end=' ')
