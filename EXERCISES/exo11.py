#WAP to make a multiplication table for any given number
num = int(input("Enter a value: "))

for i in range(1,11):
    print(num,"*",i,"=",num*i)

print()
i = 1
while i<=10:
    print(num,"*",i,"=",num*i)
    i+=1