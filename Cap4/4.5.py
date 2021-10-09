su=0
nu =int(input("nu="))
c=1
while True:
    ed =int(input("ed="))
    su+=ed
    c=c+1
    if(c>nu):
        break
pr=su/nu
print("edad promedio del grupo: ", pr)