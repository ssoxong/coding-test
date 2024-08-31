import heapq
import sys
input = sys.stdin.readline

global graph

def dijkstra(start, dst):
    global graph
    n = len(graph)
    q = []
    dist = [1e9]*(n+1)

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        nd, now = heapq.heappop(q)
        if dist[now]<nd: continue

        for g in graph[now]:
            w, b = g[1], g[0]
            cost = nd+w

            if cost<dist[b]:
                dist[b]=cost
                heapq.heappush(q, (cost, b))
                
    return dist[dst]

n, m, x = map(int,input().split())
graph = [[]for i in range(n+1)]
std = set()
for i in range(m):
    a, b, w = map(int,input().split())
    graph[a].append((b,w))
    std.add(a)

ans = 0
for i in std:
    ans = max(ans, dijkstra(i, x)+dijkstra(x, i))

print(ans)