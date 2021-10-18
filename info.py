# echo "# Proyecto-Python-UAB" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/itorricom/Proyecto-Python-UAB.git
# git push -u origin main


# Funciones Lambda: +++++++++++++++++++++

def doblar(num): return num*2


doblar(2)
4


def impar(num): return num % 2 != 0


impar(5)
True

numerosA = [1, 2, 3, 4, 5]
numerosB = [6, 7, 8, 9, 10]
resultado = list(map(lambda x, y: x + y, numerosA, numerosB))
print(resultado)

# Funciones Filter: +++++++++++++++++


def numero_par(num):
    if num % 2 == 0:
        return True


numeros = [17, 24, 7, 39, 8, 51, 92]
print(list(filter(numero_par, numeros)))

numeros = [17, 24, 7, 39, 8, 51, 92]
print(list(filter(lambda numero_par: numero_par % 2 == 0, numeros)))


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


# Funciones Map: +++++++++++++++++

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleado = [
    Empleado("Roy", "Director", 6700),
    Empleado("Lili", "Directora", 7500),
    Empleado("Darwin", "Jefe", 2100),
    Empleado("Jhoan", "Dev", 2150),
    Empleado("Roy", "Test", 1800)
]


def calculo_comision(empleado):
    empleado.salario = empleado.salario*1.03
    return empleado


listaEmpleadosComision = map(calculo_comision, listaEmpleado)

for empleado in listaEmpleadosComision:
    print(empleado)
