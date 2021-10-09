N = int(input("N="))
TI = str(input("TI="))
TP = str(input("TP="))
if TI == "Sencilla":
    PA = 20
else:
    if TI == "Doble":
        PA = 25
    else:
        PA = 28
TO = PA*N
if TP == "TAR":
    CA = TO*0.05
else:
    CA = 0
TOT = TO + CA
print("La hamburguesa costo: ", PA)
print("El total sin cargo es: ", TO)
print("El Cargo es: ", CA)
print("El total por pagar es: ", TOT)
