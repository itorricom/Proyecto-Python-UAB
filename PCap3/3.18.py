antiguedad = int(input("antiguedad:"))
sueldo = int(input("sueldo:"))
if antiguedad > 4 or sueldo < 2000:
    bono = sueldo*0.25
else:
    bono = sueldo*0.20
print(bono)
