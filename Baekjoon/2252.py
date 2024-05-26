n, m = map(int,input().split())
arr=[[] for _ in range(n+1)]
ine = [0]*(n+1)
q = []
line = []
for i in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    ine[b]+=1

for i in range(1, n+1):
    if ine[i]==0:
        q.append(i)

while(len(q)>0):
    v = q.pop(0)
    line.append(v)
    for i in arr[v]:
        if ine[i]-1==0:
            q.append(i)
        ine[i]-=1
    arr[v].clear()

print(*line)