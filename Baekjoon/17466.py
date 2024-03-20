import math

n,p = map(int,input().split())
mul = 1

for i in range(1, n+1):
    mul = (mul*i)%p

print(mul)