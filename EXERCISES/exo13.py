# 13/ with given list l=["a","b","c","d"] write a program to get this output
#     0-a 
#     1-b
#     2-c
#     3-d

l=["a","b","c","d"]

for i in range(len(l)):
    print(i, '-', l[i])