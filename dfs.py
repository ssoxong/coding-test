n = 4
m = 5
v = 1
graph = [[1,2],[1,3],[1,4],[2,4],[3,4]]
boolg = [[False]*n for _ in range(n)]
visited = [False]*(n+1)

for g in range (len(graph)):
    s,e = graph[g]
    boolg[s-1][e-1]=True
    boolg[e-1][s-1]=True

def dfs(v):

    visited[v] = True
    print(v)
    for index, go in enumerate(boolg[v-1]):
        if go and not visited[index+1]:
            dfs(index+1)

dfs(v)