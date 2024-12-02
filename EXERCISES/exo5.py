#WAP to make a grade of students according to their marks in 5 subjects

def inputCheck(a):
    while a < 0 or a > 100:
        a = float(input("Range is between 0-100, enter valid range: "))
    return a

print("Enter the marks for the different subjects out of 100: ")

math = inputCheck(float(input("Enter the marks for mathematics: ")))
inputCheck(math)
phy = inputCheck(float(input("Enter the marks for physics: ")))
inputCheck(phy)
chem = inputCheck(float(input("Enter the marks for chemistry: ")))
inputCheck(chem)
eng = inputCheck(float(input("Enter the marks for english: ")))
inputCheck(eng)
sci = inputCheck(float(input("Enter the marks for science: ")))
inputCheck(sci)

total = math + phy + chem + sci + eng
percentage = total / 5

if percentage >= 90 and percentage <= 100:
    print("Outstanding")
elif percentage >= 80 and percentage < 90:
    print("A+")
elif percentage >= 70 and percentage < 80:
    print("A")
elif percentage >= 60 and percentage < 70:
    print("B+")
elif percentage >= 50 and percentage < 60:
    print("B")
elif percentage >= 40 and percentage < 50:
    print("Pass")
else:
    print("Fail")





