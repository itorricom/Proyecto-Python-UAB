A = float(input("A="))
B = float(input("B="))
C = float(input("C="))
if A > B:
    if A > C:
        M = A
    else:
        M = C
else:
    if B > C:
        M = B
    else:
        M = C
print("El mayor es:", M)
