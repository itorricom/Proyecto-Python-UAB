precioProducto = int(input("precioProducto:"))
if precioProducto >= 200:
    descuento = precioProducto * 0.15
else:
    if precioProducto > 100 and precioProducto < 200:
        descuento = precioProducto * 0.12
    else:
        descuento = precioProducto * 0.10
precioProducto = precioProducto - descuento
print("El costo del articulo es: ", precioProducto)
print("El descuento es: ", descuento)
