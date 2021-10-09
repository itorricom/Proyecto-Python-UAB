sueldo = int(input("sueldo:"))
antiguedad = int(input("antiguedad:"))
if antiguedad > 2 and antiguedad < 5:
    bonoAntiguedad = sueldo * 0.20
else:
    if antiguedad > 5:
        bonoAntiguedad = sueldo * 0.30
if sueldo < 1000:
    bonoSueldo = sueldo * 0.25
else:
    if sueldo > 100 and sueldo < 3500:
        bonoSueldo = sueldo * 0.15
    else:
        bonoSueldo = sueldo * 0.10
print("El bono de antiguedad es: ", bonoAntiguedad)
print("El bono por concepto de sueldo es: ", bonoSueldo)
