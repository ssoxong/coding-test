import heapq

def solution(n, costs):
    answer = 0
    con = [[] for _ in range(n)]

    for c in costs:
        con[c[0]].append((c[1], c[2]))
        con[c[1]].append((c[0], c[2]))
    q=[]
    visited = [False] * (n+1)
    for c in con[0]:
        heapq.heappush(q, (c[1], c[0]))
    visited[0]=True

    while(q):
        w, e = heapq.heappop(q)
        if visited[e]: continue
        visited[e]=True
        answer+=w

        for c in con[e]:
            heapq.heappush(q, (c[1], c[0]))
        
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]	))