pasaje = int(input("pasaje:"))
costoKilometro = 3
pasajeMexico = 750*3
pasajePv = 800*3
pasajeAcapulco = 1200*3
pasajeCancun = 1800*3
if(pasaje >= pasajeMexico and pasaje < pasajePv):
    lugar = "Mexico"
else:
    if(pasaje >= pasajePv and pasaje < pasajeAcapulco):
        lugar = "PV"
    else:
        if(pasaje >= pasajeAcapulco and pasaje < pasajeCancun):
            lugar = "Acapulco"
        else:
            if(pasaje >= pasajeCancun):
                lugar = "Cancun"
            else:
                lugar = "Quedate en casa"
print("Lugar de destino :", lugar)
