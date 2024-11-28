#WAP to perform arithmetic operation on 2 integers using conditional statement

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("""
    Chose any number for operation:
        1- Add
        2- Sub
        3- Mult
        4- Div
        """)
choice = int(input())

if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice == 4:
    while b==0:
        b = int(input("2nd number cannot be 0, Enter new number: "))    
    print(a//b)
else:
    print("Invalid choice")
