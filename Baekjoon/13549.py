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

n, k = map(int,input().split())
graph = [[]for i in range(100001)]

# graph 전처리
for i in range(0, 100001):
    if i+1<100001:
        graph[i].append((i+1, 1))
    if i-1>=0:
        graph[i].append((i-1, 1))
    if i*2<100001:
        graph[i].append((i*2, 0))

print(dijkstra(n, k))