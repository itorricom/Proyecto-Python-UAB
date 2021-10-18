n, q = map(int, input().split())
libros = list(map(int, input().split()))
libros.sort()
idlibros = list(map(int, input().split()))
for i in idlibros:
    for j in range(0, n):
        if i == libros[j]:
            print(j, end=' ')
