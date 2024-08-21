import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

n = int(input().strip())
arr=[]
for i in range(n):
    tmp = list(input().strip())
    for i in range(len(tmp)):
        if tmp[i]=='R':
            tmp[i]=0
        if tmp[i]=='G':
            tmp[i]=1
        if tmp[i]=='B':
            tmp[i]=2

    arr.append(tmp)

cnt=0
rgb=[0,0,0]
rrb=[0,0,0]

def dfs(start, a, b):
    if arr[a][b] not in start:
        return
    visited[a][b]=True

    if a-1>=0 and not visited[a-1][b]:
        dfs(start, a-1, b)
    if b-1>=0 and  not visited[a][b-1]:
        dfs(start, a, b-1)
    if a+1<n and not visited[a+1][b]:
        dfs(start, a+1, b)
    if b+1<n and  not visited[a][b+1]:
        dfs(start, a, b+1)

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        cnt = 0
        if not visited[i][j]:
            dfs([arr[i][j]], i, j)
            rgb[arr[i][j]]+=1

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        cnt = 0
        if not visited[i][j]:
            if arr[i][j]==0 or arr[i][j]==1:
                start=[0,1]
            else:
                start=[2]
            dfs(start, i, j)
            rrb[arr[i][j]]+=1

print(sum(rgb), sum(rrb))
            
