n =int(input("n="))

a=0
b=1
print(a)
print(b)
m=1
while m <= (n-2):
    c=a+b
    print(c)
    a=b
    b=c
    m+=1
