import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
V, E = map(int,input().split())
snode = int(input())
graph = [[] for _ in range(V+1)]

def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+ i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


distance = [inf] * (V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dijkstra(snode)

for i in range(1,V+1):
    if distance[i] == inf:
        print("INF")
    else:
        print(distance[i])