lowerLimit=int(input("Enter lowerLimit >0: "))
while lowerLimit<0:
    lowerLimit=int(input("Enter lowerLimit >0: "))
upperLimit=int(input("Enter upperLimit > lowerLimit: "))
while upperLimit<lowerLimit:
    upperLimit=int(input("Enter upperLimit > lowerLimit: "))
k=1
for i in range (lowerLimit, upperLimit):
    num=i
    num1=0
    while num>0:
        digit = num % 10
        num1= num1+digit
        num=num//10
        if num>0:
            num1=num1*10
    if i==num1:
        print(i, end=" ")
        k=k+1
    if k%6==0:
        print()
        k=1
        
    

