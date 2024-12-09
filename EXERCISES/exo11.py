# WAP to calculate the square of even and cube of odd from 1 to 20 using list

l=[]
m=[]

for i in range(1,21):
    if(i%2==0):
        l.append(i**2)
    else:
        m.append(i**3)

print(l)
print(m)