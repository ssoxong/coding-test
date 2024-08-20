import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    dist = [1e9]*(n+1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start]=0

    while q:
        nd, now = heapq.heappop(q)
        if dist[now]<nd: continue
        for g in graph[now]:
            w, b = g[1], g[0]
            cost = nd+w
            if cost<dist[b]:
                dist[b] = cost
                heapq.heappush(q, (cost, b))
    return dist

n, e = map(int,input().split())
graph = [[]for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
u,v = map(int,input().split())

dist = dijkstra(1)
dist_u = dijkstra(u)
dist_v = dijkstra(v)

ans = 1e9
ans = min(dist[u]+dist_u[v]+dist_v[n], dist[v]+dist_v[u]+dist_u[n])
if ans>=1e9:
    print(-1)
else:
    print(ans)