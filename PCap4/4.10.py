cantidadSalones = int(input("cantidadSalones:"))
edadPromedioSalon = 0
edadPromedioEscuela = 0
for i in range(cantidadSalones):
    cantidadEdades = int(input("cantidadEdades:"))
    sumaEdades = 0
    for j in range(cantidadEdades):
        edad = int(input("edad:"))
        sumaEdades = sumaEdades + edad
    edadPromedioSalon = sumaEdades / cantidadEdades
    edadPromedioEscuela += edadPromedioSalon
    print("Edad promedio del salon es: ", edadPromedioSalon)
print("Edad promedio de la escuela es: ", edadPromedioEscuela)
