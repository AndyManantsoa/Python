#WAP to use identity operator

a,b=2,2
print(id(a))
print(id(b))

b=3 #string is mutable in python
print(id(b))
print(a is b)