visited = []
def dfs(i, computers):
    global visited
    visited[i] = True
    for j, con in enumerate(computers[i]):
        if con==1:
            if visited[j]: continue
            dfs(j, computers)


def solution(n, computers):
    global visited
    visited = [False]*n
    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, computers)
            ans+=1

    return ans

print(solution(3	,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))