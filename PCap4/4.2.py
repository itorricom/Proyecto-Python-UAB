numeroHamburguesas = int(input("numeroHamburguesas:"))
tipo = str(input("tipo:"))
tipoPago = str(input("Pago con Tarjeta(s/n):"))

if tipo == "s":
    costo = 20
else:
    if tipo == "d":
        costo = 25
    else:
        if tipo == "t":
            costo = 28
montoPagar = costo * numeroHamburguesas
if tipoPago == "s":
    cargo = montoPagar * 0.5
montoPagar = cargo + montoPagar
print("Monto a pagar es:", montoPagar)
