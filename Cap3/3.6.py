NP = int(input("NP="))
if NP > 300:
    TOT = NP*75
else:
    if NP > 200:
        TOT = NP*85
    else:
        TOT = NP*95
print("Total es: ", TOT)
