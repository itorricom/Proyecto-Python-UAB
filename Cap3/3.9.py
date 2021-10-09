TI = int(input("TI="))
DI = str(input("DI="))
TU = str(input("TU="))
if TI < 5:
    PAG = TI*1
else:
    if TI < 8:
        PAG = (TI-5)*0.8+5
    else:
        if TI <= 10:
            PAG = (TI-8)*0.7+7.4
        else:
            PAG = (TI-10)*0.5+8.8
if DI == "DOM":
    IMP = PAG*0.05
else:
    if TU == "M":
        IMP = PAG*0.15
    else:
        IMP = PAG*0.10
TOT = PAG+IMP
print("El pago es:", PAG)
print("El impuesto es:", IMP)
print("El total es:", TOT)
