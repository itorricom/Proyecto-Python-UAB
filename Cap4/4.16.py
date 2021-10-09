sh=0
ph =int(input("ph="))
d=1
while True:
    ht =int(input("ht="))
    sh+=ht
    d+=1
    if(d>6):
        break
su=sh*ph
print("las horas laboradas son: ",sh)
print("el sueldo es: ",su)