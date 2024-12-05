# A program that calculates the factorial of a number.

a= int(input("Enter a number"))
c=1
for i in range(a,1,-1):
    c=c*i
print(c)