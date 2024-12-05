#A program that checks if a given string is a palindrome.
a = input("Enter a string: ")

if a==a[::-1] :
    print("It is palindrome")
else:
    print('It is not palindrome')