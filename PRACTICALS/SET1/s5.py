#A program that checks if a given year is a leap year

def isLeap(year):
    if year % 4 == 0:
        return True
    elif year%400==0:
        return True
    else:
        return False

year = int(input("Enter a year: "))

if isLeap(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")