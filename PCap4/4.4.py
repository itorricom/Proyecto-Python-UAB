loteFocos = int(input("loteFocos:"))
verde, blanco, rojo = 0, 0, 0
for i in range(0, loteFocos, 1):
    colorFoco = str(input("colorFoco:"))
    if colorFoco == "v":
        verde += 1
    else:
        if colorFoco == "r":
            rojo += 1
        else:
            if colorFoco == "b":
                blanco += 1
            else:
                print("El color no existe")
print("Cantidad de focos rojos: ", rojo)
print("Cantidad de focos verdes: ", verde)
print("Cantidad de focos blancos: ", blanco)
