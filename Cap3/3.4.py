CT = int(input("CT="))
if CT > 2500:
    DE = CT*0.15
else:
    DE = CT*0.08
PF = CT-DE
print("El final es: ", PF)
print("Descuento es: ", DE)
