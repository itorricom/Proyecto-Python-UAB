cp=0
cn=0
nu =float(input("nu="))
c=1
while True:
    ca =float(input("ca="))
    if ca > 0:
        cp+=1
    else:
        cn+=1
    c+=1
    if(c > nu):
        break
print("positivos: ",cp)
print("negativos: ",cn)