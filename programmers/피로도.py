ans = []

def dfs(k, i, cnt, dun, visited):
    global ans

    d = dun[i]
    if k<d[0]: ans.append(cnt-1); return
    visited[i] = True

    for j in range(len(dun)):
        if visited[j]: continue
        dfs(k-d[1], j, cnt+1, dun, visited)
        visited[j] = False
        
    if cnt==len(dun): ans.append(cnt)

def solution(k, dun):
    global ans
    visited = [0 for _ in range(len(dun))]

    for i in range(len(dun)):
        dfs(k, i, 1, dun, visited)
        visited[i]=False

    return max(ans)

print(solution(80,	[[80,20],[50,40],[30,10]]))