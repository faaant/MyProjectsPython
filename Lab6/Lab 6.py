from math import sqrt 

def square (a,b,c):              #Calculating the area of the triangle
    def pivP (a,b,c):             #Calculating half-perimetr
        return (a+b+c)/2
    p= pivP(a,b,c)
    return sqrt(p*(p-a)*(p-b)*(p-c))
s1=0.0
for i in range (1,4):            #Entering sides of triangles
    a=float(input ("Enter first side of triangle: "))
    a1=float(input ("Enter second side of triangle: "))
    a2=float(input ("Enter third side of triangle: "))
    while (a<=0) or (a1<=0) or (a2<=0):         #Data verification
        print ("Enter correct sides!\n")
        a=float(input ("Enter first side of triangle: "))
        a1=float(input ("Enter second side of triangle: "))
        a2=float(input ("Enter third side of triangle: "))
    s = square(a,a1,a2)
    if (s>s1):       #Number of triangle with the largest square
        n=i
        s1=s
    if (s>0):
        print ("s= ",s, end="\n\n")
    else:
        print ("Triangle does not exist!",end="\n\n")
print (n,"triangle has the largest area.")
