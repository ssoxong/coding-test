from collections import deque
def solution(tickets):
    tickets.sort(key=lambda x:(x[0], x[1]))

    q = deque()
    q.append(('ICN', ['ICN'], [0]*len(tickets) ))
    while(q):
        # print(q)
        cur, travel, visited = q.popleft()

        if len(travel)==len(tickets)+1:
            return travel
        
        for i, t in enumerate(tickets):
            if not visited[i] and cur==t[0]:
                nv = visited[:]
                nv[i]=1
                q.append((t[1], travel+[t[1]], nv))

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
