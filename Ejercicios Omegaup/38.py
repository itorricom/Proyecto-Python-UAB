n = int(input())
secuecia = list(map(int, input().split()))
secuecia.reverse()
for s in secuecia:
    print(s, end=' ')
