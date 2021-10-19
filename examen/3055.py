num = int(input())
cadena = []
for i in range(num):
    t, l = map(int, input().split())
    if l % t == 0:
        cadena.append('R')
    else:
        cadena.append("I")
for i in range(num):
    print(cadena[i])


""" num = int(input())
for i in range(num):
    t, l = map(int, input().split())
    if l % t == 0:
        print('R')
    else:
        print("I") """
