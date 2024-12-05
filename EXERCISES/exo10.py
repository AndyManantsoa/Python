#WAP to make a simple log in authentication page using conditional statement

email = input("Enter your email: ")
password = input("Enter your password: ")

while email != "abc@email.com" or password !="123":
    if email != "abc@email.com" :
        email = input("Email invalid, Enter your email: ")
    elif password !="123" :
        password = input("Password invalid, Enter your password: ")

if email == "abc@email.com" or password =="123":
    print('Login successful')