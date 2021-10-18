listaNumeros = []
while True:
    numero = int(input())
    if numero == 0:
        break
    else:
        listaNumeros.append(numero)
for i in listaNumeros:
    suma = 0
    for j in range(1, i+1):
        suma = suma + j
    print(suma)


class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleado = [
    Empleado("Roy", "Director", 750000),
    Empleado("Lili", "Directora", 650000),
    Empleado("Darwin", "Jefe", 550000),
    Empleado("Jhoan", "Dev", 450000),
    Empleado("Roy", "Test", 350000)
]

salario_altos = filter(
    lambda empleado: empleado.salario > 500000, listaEmpleado)

for empleado_salario in salario_altos:
    print(empleado_salario)
