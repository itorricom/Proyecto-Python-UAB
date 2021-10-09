import math
R = float(input("AlturaTriangulo="))
H = float(input("Base="))
C = math.sqrt(H*H - R*R)
AT = 2*(R*C)/2
AC = (3.1416*R*R)/2
Area = AT*AC
print(Area)
