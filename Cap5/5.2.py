"""
Se requiere obtener la suma de las cantidades contenidas en un arreglo de
10 elementos. Realice el algoritmo y represéntelo mediante el diagrama
de flujo, el pseudocódigo y el diagrama N/S.
I Contador y subíndice entero , VA Nombre del vector de valores real, SU Suma de los valores real
"""
va = []
for i in range(0, 10):
    va.append(float(input("va:")))

su = 0
for i in range(0, len(va)):
    su = su + va[i]
print("La suma es: ", su)
