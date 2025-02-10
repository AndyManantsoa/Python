# WAP to slice a string and use various string functions
# string slicing: frontward(positive) & backward(negative)
# varname[start:end+1:step], by default [0:long:1]

a = "Manantsoa ClaudiNo"

print(a[1:8:2].upper())
print(a[4:1:-1].lower())
print(a[-1:-4:-1].title())  # first char is in capitalx
print(a.index("n", 3))  # returns error if char is not found,
print(a.lower().count("n"))

try:
    print(a.index("j"))
except ValueError:
    print("Error")

print(a.find("j"))  # returns -1 if char is not found

# membership operator
print("f" in a)
print("A".lower() in a)
