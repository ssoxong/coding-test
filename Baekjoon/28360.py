n, m = map(int,input().split())
arr = [[] for _ in range(55)]
d = [0 for _ in range(55)]
d[1] = 100
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
ans=[]
for i in range(1, n+1):
    if len(arr[i])==0: continue
    for j in arr[i]:
        d[j]+= d[i]/len(arr[i])
    d[i]=0

print(max(d))