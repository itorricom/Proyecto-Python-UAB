TI = str(input("TI="))
TA = int(input("TA="))
P = float(input("P="))
K = int(input("K="))
if TI == "A":
    if TA == 1:
        P = P+0.20
    else:
        P = P+0.30
else:
    if TA == 1:
        P = P-0.30
    else:
        P = P-0.50
GA = P*K
print("La ganancia es:", GA)
