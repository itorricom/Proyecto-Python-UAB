n = int(input())
m = list(map(int, input().split()))
dinero = 0
for x in range(0, n):
    it = m[x]
    suma = 0
    for i in range(1, it+1):
        suma = suma + i
    dinero = dinero + suma
print(dinero)

""" 5
1 2 3 4 5
 
1  1+2=3  1+2+3=6  1+2+3+4=10  1+2+3+4+5=15

por lo tanto 1+3+6+10+15=35 

Si tienen 2 tarjetas, una con 6 números y otra con 13 el dinero que obtendrían sería de 112 por 
que 1+2+3+4+5+6=21 y 1+2+3+4+5+6+7+8+9+10+11+12+13=91 por lo tanto 21+91=112.

"""
