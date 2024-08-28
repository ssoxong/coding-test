arr = list(map(int,input().split()))
ans = 0
for a in arr:
    ans+=a**2
print(ans%10)