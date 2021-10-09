horas = int(input("horas:"))
if horas <= 2:
    montoACobrar = horas*5
else:
    if horas <= 5:
        montoACobrar = ((horas - 2)*4)+10
    else:
        if horas <= 10:
            montoACobrar = ((horas-7)*3)+22
        else:
            montoACobrar = ((horas - 10)*2)+37
print("Monto a cobrar es: ", montoACobrar)
