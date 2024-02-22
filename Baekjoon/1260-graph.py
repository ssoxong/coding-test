# DFS와 BFS

def bfs(graph, visited, arr, start):
    arr.append(start)

    while(len(arr)>0):
        a = arr.pop(0)
        if(visited[a-1]):
            continue
        visited[a-1]=True
    
        print(a, end=" ")

        for index, g in enumerate(graph[a-1]):
            if g:
                arr.append(index+1)

def dfs(graph, visited, a):
    if(visited[a-1]):
        return
    
    visited[a-1]=True
    print(a, end=" ")

    for index, g in enumerate(graph[a-1]):
        if g:
            dfs(graph, visited, index+1)
            
n, m, v = map(int, input().split())
graph = [[False for _ in range(n)]for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1]=True
    graph[b-1][a-1]=True

visited=[False]*n
dfs(graph, visited, v)
print()

arr=[]
visited=[False]*n
bfs(graph, visited, arr, v)
