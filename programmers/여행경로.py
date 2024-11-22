from collections import deque

def solution(tickets):
    tickets.sort(key=lambda x:(x[0], x[1]))
    visited = [0 for _ in range(len(tickets))]

    def dfs(cur, travel):
        nonlocal tickets, visited

        if len(travel)==len(tickets)+1:
            return travel
        
        for i, t in enumerate(tickets):
            if not visited[i] and cur==t[0]:
                visited[i]=1
                res = dfs(t[1], travel+[t[1]])
                visited[i]=0
                if res: return res

    return dfs("ICN", ["ICN"])

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))