#WAP to calculate the sum of all numbers from 1 to 11 using list

l=[]

for i in range(1,11):
    l.append(i)

print(l)

for i in l:
    if i%2==0:
        print(i, end=", ")


sum =0

for i in range(len(l)):
    sum= l[i] +sum

# for i in l:
#     sum= i +sum

print(sum)
