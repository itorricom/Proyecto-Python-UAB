puntuacion = int(input("puntuacion:"))
salario = int(input("salario:"))
if puntuacion >= 0 and puntuacion <= 100:
    bono = salario
else:
    if puntuacion >= 101 and puntuacion <= 150:
        bono = salario*2
    else:
        bono = salario*3
print(bono)
