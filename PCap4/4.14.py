numAlumnos = int(input("numAlumnos:"))
aprobados = 0
reprbados = 0
for i in range(numAlumnos):
    nota = int(input("nota:"))
    if nota > 51:
        aprobados = aprobados + 1
    else:
        reprbados += 1
print("Aprobados: ", aprobados)
print("Reprobados: ", reprbados)
