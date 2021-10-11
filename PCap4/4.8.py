numeroArticulos = int(input("numeroArticulos:"))
pagoTotal = 0
for i in range(numeroArticulos):
    precio = int(input("precio:"))
    if precio >= 200:
        descuento = precio * 0.15
    else:
        if precio > 100 and precio < 200:
            descuento = precio * 0.12
        else:
            descuento = precio * 0.10
    costo = precio - descuento
    pagoTotal += costo
    print("El descuento es:", descuento)
    print("El costo es:", costo)
print("El pago total es: ", pagoTotal)
