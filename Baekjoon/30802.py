n = int(input())
arr = list(map(int,input().split()))
t, p = map(int,input().split())
tt = 0
for a in arr:
    tt += a//t
    if a%t != 0: tt+=1
    
pp = n//p
ppp = n%p

print(tt)
print(pp, ppp)