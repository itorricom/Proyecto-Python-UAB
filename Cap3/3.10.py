TI = str(input("TI="))
KM = int(input("KM="))
NPR = int(input("NPR="))
if TI == "A":
    CK = 2
else:
    if TI == "B":
        CK = 2.50
    else:
        CK = 3.0
if NPR < 20:
    NP = 20
else:
    NP = NPR
TO = NP*CK*KM
CP = TO/NPR
print("La persona pagara: ", CP)
print("El costo del viaje es: ", TO)
