#WAP to check how many numbers are divisible by 5 from  0-100

i=0
sum =0
while i<=100 :
    if i%5==0 :
        sum+=1
    i+=1

print('There are ',sum, 'divisible by 5 in the range of 0 to 100')