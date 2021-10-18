K = float(input())
N = int(input())
suma = 0
for i in range(1, N+1):
    nota = float(input())
    suma = suma + nota
if suma/N > K:
    print("Presume")
else:
    print("Ladra")
