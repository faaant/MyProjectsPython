n=int(input("n must be >0. Enter number n = "))
while n<=0:
    n=int(input("n must be >0. Enter number n = "))
a=float(input("Enter number a = "))
b=float(input("Enter number b(!=a) = "))
while (b-a)==0:
    b=float(input("Enter number b(!=a) = "))
h=(b-a)/n
for i in range(1,n+1):
    r=a+i*h
    print(r,end=" ")

    
