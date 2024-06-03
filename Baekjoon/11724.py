def bfs(v):
    global ans
    if visited[v]: return
    ans+=1
    q = []
    q.append(v)
    visited[v]=1
    while len(q):
        v = q.pop(0)
        for i in graph[v]:
            if visited[i]: continue
            q.append(i)
            visited[i]=1
            
n, m = map(int,input().split())
visited=[0 for _ in range(n+1)]
graph=[[]for _ in range(n+1)]
ans=0

for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    bfs(i)

print(ans)