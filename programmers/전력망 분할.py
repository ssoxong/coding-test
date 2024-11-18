def bfs(graph, w):
    visited = [0 for _ in range(len(graph))]
    
    
    graph[w[0]][w[1]]=0
    graph[w[1]][w[0]]=0

    q = []
    q.append(w[0])
    cnt1 = 0
    while(q):
        ww = q.pop(0)
        cnt1+=1
        visited[ww] = 1
        for i in range(len(graph)):
            if visited[i]: continue
            if graph[ww][i]==1:
                q.append(i)

    q = []
    q.append(w[1])
    cnt2 = 0
    visited = [0 for _ in range(len(graph))]

    while(q):
        ww = q.pop(0)
        cnt2+=1
        visited[ww] = 1
        for i in range(len(graph)):
            if visited[i]: continue
            if graph[ww][i]==1:
                q.append(i)

    return abs(cnt1-cnt2)


def solution(n, wires):
    graph = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for a, b in wires:
        graph[a][b]=1
        graph[b][a]=1

    cha = []
    tmpg = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for w in wires:
        for i in range(0, n+1):
            tmpg[i] = graph[i].copy()

        cha.append(bfs(tmpg, w))

    return min(cha)

print(solution(9,	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))