q= float(input("Use \'.\' no \',\' \nEnter q= ")) #Enter the accuracy of calculations
sum=1.0
i=0;
sum1=0.0
factorial=1.0
while abs(sum-sum1)>q:
    i=i+1
    factorial=factorial*i #Searching i!
    Number=1/factorial #Searching Number
    sum1=sum
    sum=sum+Number #Searching sum of Numbers
print(sum) #output
