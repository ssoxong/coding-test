n, m = map(int,input().split())
g = [[]for _ in range(1010)]
ii = [0 for _ in range(1010)]
d= [0 for _ in range(1010)]
for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    ii[b]+=1

check=[]
for i in range(1, n+1):
    if 0 == ii[i]:
        check.append(i)
        d[i]=1
    
while len(check)>0:
    v = check.pop(0)
    for i in g[v]:
        d[i] = max(d[i], d[v]+1)
        if ii[i]-1==0:
            check.append(i)
        ii[i]-=1

for i in d:
    if i==0: continue
    print(i, end=" ")

