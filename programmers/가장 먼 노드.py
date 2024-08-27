from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[]for _ in range(n+1)]
    
    for e in edge:
        x, y = e[0], e[1]
        graph[x].append(y)
        graph[y].append(x)
        
    distance = [0 for _ in range(n+1)]
    
    q = deque()
    q.append(1)
    distance[1]=1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if distance[i]: continue
            distance[i] = distance[x]+1
            q.append(i)
    
    _max = max(distance)
    return distance.count(_max)