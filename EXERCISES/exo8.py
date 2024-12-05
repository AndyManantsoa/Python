#WAP to slice a string
#string slicing: frontward(positive) & backward(negative)
#varname[start:end+1:step], by default [0:long:1]

a="python"

print(a[1:4:2])
print(a[4:1:-1])
print(a[-1:-4:-1])

print(a[-1:1:-1])
print(a[-2:2:-2])
print(a[2:1:1])
print(a[-1::-1])
print(a[::-1])
print(a[2:6:-1])