email = input("Enter email: ")
emailCheck= email.endswith("@gmail.com")
while not emailCheck:
    email = input("Incorrect email. Enter agin email: ")

pwd = input("Enter password: ")
pwdCheck = pwd.isdigit
while not pwdCheck :
    pwd = input("Password must be a digit, Enter again password: ")

repwd = input("ReEnter password: ")

while pwd != repwd :
    repwd = input("Password not matching, Enter again password: ")

if pwdCheck and emailCheck and repwd:
    print("Registered successfuly")