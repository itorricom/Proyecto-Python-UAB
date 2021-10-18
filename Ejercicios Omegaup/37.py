p = int(input())
n = int(input())
suma = 0
for i in range(n):
    x = int(input())
    suma = suma + x
cant = int(suma/p)
resta = suma % p
print(cant, '', resta)

""" 
3
2
5
6

3 2 """
