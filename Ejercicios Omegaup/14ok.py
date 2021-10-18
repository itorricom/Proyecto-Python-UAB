n = int(input())
listaB = []
if n > 500 or n < 0:
    print("Error")
else:
    b = 0
    while n >= 1:
        b = n % 2
        n = int(n/2)
        listaB.append(b)
listaB.reverse()
for item in listaB:
    print(item)
