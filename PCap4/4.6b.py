salario = 1500
for c in range(6):
    incremento = salario * 0.10
    totalSalario = salario + incremento
    salario = totalSalario
    print("Salario del año ", c+1, " es: ", totalSalario)

print("Salario final al 6 año es: ", salario)
