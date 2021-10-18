califDada = int(input("califDada:"))
if califDada >= 0 and califDada <= 5:
    califDada = 'F'
else:
    if califDada == 10:
        califDada = 'A'
    elif califDada == 9:
        califDada = 'B'
    elif califDada == 8:
        califDada = 'C'
    else:
        califDada = 'D'
print(califDada)
