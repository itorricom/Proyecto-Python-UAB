salario = 1500
contador = 1
while True:
    incremento = salario * 0.10
    totalSalario = salario + incremento
    salario = totalSalario
    print("Salario del año ", contador, " es: ", totalSalario)
    contador += 1
    if contador > 6:
        break
print("Salario final al 6 año es: ", salario)
