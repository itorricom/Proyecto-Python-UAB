tamanio = int(input())
palabra = str(input())

if tamanio > 10:
    inicio = palabra[0]
    fin = palabra[tamanio-1]
    print(inicio+str(tamanio-2)+fin)
else:
    print(palabra)
