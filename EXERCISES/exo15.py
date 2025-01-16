#WAP to find a particular char in a string and count the number of occurences of that char in the string.
s="I am a string"

a=input("Enter character to find: ")

count = 0

for i in s:
    if a==i:
        count+=1

print(count)