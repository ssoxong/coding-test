from collections import deque

def solution(n, edge):
    graph = [[]for _ in range(n+1)]
    dis = [-1 for _ in range(n+1)]
    dis[1] = 1
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q=[]
    q.append(1)

    while q:
        cur = q.pop(0)
        for g in graph[cur]:
            if dis[g]!=-1: continue
            dis[g] = dis[cur]+1
            q.append(g)

    return dis.count(max(dis))

print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))

