#Check if a XXXX year is leap or not

def isLeap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year = int(input("Enter a year: "))

if isLeap(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


