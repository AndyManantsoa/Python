#WAP to compare the height of 3 numbers

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

if n1>=n2 and n1>=n3:
    print(n1, "is greater")
elif n2>=n1 and n2>=n3:
    print(n2, "is greater")
else :
    print(n3, "is greater")
