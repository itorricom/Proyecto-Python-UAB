import math
horasUso = float(input("horasUso="))
tarifa = 6
horaCompleta = math.ceil(horasUso)
totalPago = tarifa * horaCompleta
print("El costo del parque es: ", totalPago)
