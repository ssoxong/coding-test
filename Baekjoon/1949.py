import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
a=[0]

g = [[]for _ in range(n+1)]
d = [[0 for _ in range(2)]for _ in range(n+1)]

def dfs(v, b):
    d[v][1]+=a[v-1]
    for i in g[v]:
        if i==b: continue
        dfs(i, v)
        d[v][0] +=max(d[i][0], d[i][1])
        d[v][1]+=d[i][0]

a = list(map(int, input().split()))

for _ in range(n-1):
    u, v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
dfs(1, -1)

print(max(d[1][0], d[1][1]))