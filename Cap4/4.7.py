su=0
es =float(input("es="))
c=0
while es>0:
    su+=es
    es = float(input("es="))
    c+=1

if c==0:
    print("no hay estaturas")
else:
    pr=su/c
print("estatura promedio es: ",pr)