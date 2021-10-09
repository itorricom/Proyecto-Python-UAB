import math
R = float(input("Base="))
H = float(input("Hipotenusa="))
C = math.sqrt(H*H - R*R)
AT = 2*(R*C)/2
AC = (3.1416*R*R)/2
Area = AT*AC
print(Area)
