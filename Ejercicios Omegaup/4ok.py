numero = int(input())
for i in range(1, numero+1):
    for j in range(0, i):
        print(i, end='')
    print()
for i in range((numero-1), 0, -1):
    for j in range(0, i):
        print(i, end='')
    print()
