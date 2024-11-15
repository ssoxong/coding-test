import heapq

def solution(land, height):
    visited = [[0 for _ in range(len(land[0]))]for _ in range(len(land))]
    answer = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = []
    heapq.heappush(q, (0,0,0))
    # q.append(0, 0, 0)
    visit_cnt=0

    while(visit_cnt<len(land)**2):
        h, i, j = heapq.heappop(q)
        if visited[i][j]==1: continue
        visited[i][j]=1
        visit_cnt+=1
        answer+=h

        for k in range(4):
            if i+dx[k]<0 or i+dx[k]>=len(land) or j+dy[k]<0 or j+dy[k]>=len(land[0]): continue

            if abs(land[i][j]-land[i+dx[k]][j+dy[k]])>height:
                heapq.heappush(q, (abs(land[i][j]-land[i+dx[k]][j+dy[k]]), i+dx[k], j+dy[k]))

            # 방문하지 않은 경우 방문하도록
            else:
                heapq.heappush(q, (0, i+dx[k], j+dy[k]))    

    return answer

land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]	
height = 3

print(solution(land, height))