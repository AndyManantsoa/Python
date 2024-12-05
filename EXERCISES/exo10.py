#WAP to check if a string is palindrome or not
a = input("Enter a string: ")

if a==a[::-1] :
    print("It is palindrome")
else:
    print('It is not palindrome')