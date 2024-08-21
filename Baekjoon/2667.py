import sys
input = sys.stdin.readline

n = int(input().strip())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().strip())))

visited = [[False for _ in range(n)]for _ in range(n)]

cnt=0
house=[]

def dfs(a, b):
    global cnt
    visited[a][b]=True
    if arr[a][b]==0:
        return
    
    cnt+=1

    if a-1>=0 and not visited[a-1][b]:
        dfs(a-1, b)
    if b-1>=0 and  not visited[a][b-1]:
        dfs(a, b-1)
    if a+1<n and not visited[a+1][b]:
        dfs(a+1, b)
    if b+1<n and  not visited[a][b+1]:
        dfs(a, b+1)

for i in range(n):
    for j in range(n):
        cnt = 0
        if arr[i][j]==1 and not visited[i][j]:
            dfs(i, j)
            house.append(cnt)

print(len(house))
for i in sorted(house):
    print(i)