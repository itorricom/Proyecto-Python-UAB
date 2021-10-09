horaTrabajado = float(input("horaTrabajado:"))
pagoHora = 8
if horaTrabajado > 40:
    sueldoSemanal = (horaTrabajado * pagoHora)*2
else:
    sueldoSemanal = horaTrabajado * pagoHora
print("Sueldo semanal es: ", sueldoSemanal)
