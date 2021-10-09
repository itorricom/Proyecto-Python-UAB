precioProducto = float(input("precioProducto="))
descuento = precioProducto*0.20
iva = precioProducto*0.15
precioConDescuento = precioProducto - descuento
precioFinal = precioConDescuento + iva
print("Precion con descuento es: ", precioConDescuento)
print("Precio final es: ", precioFinal)
