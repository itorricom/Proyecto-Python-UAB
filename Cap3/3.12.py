NC = int(input("NC="))
if NC <= 3:
    CC = 200
    TOT = NC*CC
else:
    if NC <= 5:
        CC = 150
        TOT = (NC-3)*CC+600
    else:
        if NC <= 8:
            CC = 100
            TOT = (NC-5)*CC+900
        else:
            CC = 50
            TOT = (NC-8)*CC+1200
print("El costo de la consulta es: ", CC)
print("El costo del tratamiento es: ", TOT)
