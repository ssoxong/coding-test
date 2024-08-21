visited = []
graph = [[]]
score=0
ans=[]

def dfs(start, info):
    global visited, graph, score
    visited[start]=True
    
    # 양보다 늑대가 같거나 크면 유망하지 않음
    if score+info[start]<=0:
        ans.append(score)
        return
    # 마지막 노드인 경우
    if start==len(info)+1:
        ans.append(score+info[start])
        return
    score+=info[start]
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i, info)

def solution(info, edges):
    global visited, graph

    visited = [False]*(len(info))
    graph = [[]for _ in range(len(info))]
    
    for i in range(0, len(info)):
        if info[i]==0:
            info[i]=1
        else:
            info[i]=-1
    
    for e in edges:
        graph[e[0]].append(e[1])

    dfs(0, info)
    print(ans)
    answer = max(ans)
    print(answer)
    return answer


info=[0,0,1,1,1,0,1,0,1,0,1,1]	
edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

solution(info, edges)