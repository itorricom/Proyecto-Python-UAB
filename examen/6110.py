d, w = map(int, input().split())
numiricos = []
enterales = []
buscado = 0
contador = 1
for i in range(0, d):
    n, e = map(int, input().split())

    numiricos.append(n)
    enterales.append(e)

while contador <= w:
    encontrado = 0
    buscado = int(input())
    for i in range(d):
        if buscado == numiricos[i]:
            print(enterales[i])
            encontrado = 1
    if(encontrado == 0):
        print("C?")

    contador += 1
