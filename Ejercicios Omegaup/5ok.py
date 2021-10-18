nombre = str(input())
contador = 0
for caracter in nombre:
    if contador < 4:
        print(caracter, "ASCII value is ", ord(caracter))
    else:
        break
    contador += 1
