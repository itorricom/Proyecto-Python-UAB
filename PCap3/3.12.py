# -----------------------
horasTrabajadas = int(input("horasTrabajadas:"))
pagoHora = 8
if (horasTrabajadas > 50):
    print("No esta permitido trabajar esas horas")
else:
    if(horasTrabajadas >= 41 and horasTrabajadas <= 45):
        sueldoSemanal = (horasTrabajadas*pagoHora)*2
    else:
        if(horasTrabajadas >= 46 and horasTrabajadas <= 50):
            sueldoSemanal = (horasTrabajadas*pagoHora)*3
        else:
            sueldoSemanal = horasTrabajadas*pagoHora
print(sueldoSemanal)
