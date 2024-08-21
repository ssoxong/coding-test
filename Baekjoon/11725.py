import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 


n = int(input().strip())
graph = [[]for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited[start]=True
    for g in graph[start]:
        if not visited[g]:
            ans[g]=start
            dfs(g)

visited = [False]*(n+1)
dfs(1)
for i in range(2, len(ans)):
    print(ans[i])