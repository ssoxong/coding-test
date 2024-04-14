a = int(input())
b = int(input())
c = int(input())
mul = a*b*c
str = str(mul)
arr = [0]*10
for s in str:
    arr[int(s)]+=1
for a in arr:
    print(a)