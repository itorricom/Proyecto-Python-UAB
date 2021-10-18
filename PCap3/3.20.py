cantPantalones = int(input("cantPantalones:"))
costoTela = int(input("costoTela:"))
modelo = str(input("modelo:"))
if modelo == 'A':
    gastoProduccion = costoTela * 1.50
    cargo = costoTela*0.80
if modelo == 'B':
    gastoProduccion = costoTela*1.80
    cargo = costoTela*0.95
precioFinal = gastoProduccion + cargo
subTotal = precioFinal*0.30
ganancia = subTotal * cantPantalones
print("Ganara Bs", ganancia)
