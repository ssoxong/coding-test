import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, r, q = map(int,input().split())
graph = [[]for _ in range(n+1)]
ans = [1 for _ in range(n+1)]

def dfs(r, beforeRoot):
    for v in graph[r]:
        if v==beforeRoot: continue
        dfs(v, r)
        ans[r]+=ans[v]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(r, -1)

for _ in range(q):
    print(ans[int(input())])