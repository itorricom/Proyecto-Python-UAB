n = int(input())
vendidos = list(map(int, input().split()))
masv = max(vendidos)
for i in range(0, n):
    if masv == vendidos[i]:
        print(i+1, vendidos[i])
        break
