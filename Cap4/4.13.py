n =int(input("n="))
a=0
b=1
m=0
print(a)
print(b)


while True:
    c=a+b
    print(c)
    a=b
    b=c
    m = m+1
    if(m >(n-2)):
        break