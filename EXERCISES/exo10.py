#WAP to check if a string is palindrome or not
a = input("Enter a string: ")
b = a[::-1]

if a==b :
    print("It is palindrome")
else:
    print('It is not palindrome')