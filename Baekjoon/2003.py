n, m = map(int,input().split())
a = []
ans = 0
a = list(map(int,input().split()))

for i in range(n):
    j=i
    sum = 0
    while(j<n and sum<m):
        sum+=a[j]
        j+=1
    if sum==m:
        ans+=1
    sum-=a[i]

        

print(ans)