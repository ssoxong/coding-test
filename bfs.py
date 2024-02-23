n = 5
m = 5
v = 3
# graph = [[1,2],[1,3],[1,4],[2,4],[3,4]]
graph = [[5,4],[5,2],[1,2],[3,4],[3,1]]
boolg = [[False]*n for _ in range(n)]
visited = [False]*(n+1)

for g in range (len(graph)):
    s,e = graph[g]
    boolg[s-1][e-1]=True
    boolg[e-1][s-1]=True

def bfs(v):
    queue = []
    queue.append(v)
    
    while queue:
        q = queue.pop(0)
        if visited[q]:
            continue
        
        visited[q] = True
        print(q)

        for index, go in enumerate(boolg[q-1]):
            if go:
                queue.append(index+1)

bfs(v)