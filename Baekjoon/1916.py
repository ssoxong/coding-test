import heapq
import sys
input = sys.stdin.readline

global graph

def dijkstra(start, dst):
    global graph
    n = len(graph)
    q = []
    dist = [1e9]*(n+1)
    visit=[[]for _ in range(n+1)]

    heapq.heappush(q, (0, start))
    dist[start] = 0
    visit[start].append(start)

    while q:
        nd, now = heapq.heappop(q)
        if dist[now]<nd: continue

        for g in graph[now]:
            w, b = g[1], g[0]
            cost = nd+w

            if cost<dist[b]:
                dist[b]=cost
                visit[b].append(now)
                heapq.heappush(q, (cost, b))
    print(visit)
    return dist[dst]

n = int(input())
m = int(input())
graph = [[]for i in range(n+1)]

for i in range(m):
    a, b, w = map(int,input().split())
    graph[a].append((b,w))

start, dst = map(int,input().split())
print(dijkstra(start, dst))