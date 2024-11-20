from collections import deque
def solution(maps):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]

    N,M = len(maps), len(maps[0])
    visited = [[0]*M for _ in range(N)]

    q = deque([(0,0)])
    visited[0][0]=1

    while(q):
        y, x = q.popleft()
        # print(y, x, cnt)
        if y==N-1 and x==M-1: 
            return maps[y][x]

        for i in range(4):
            ddx = x+dx[i]
            ddy = y+dy[i]
            if ddx>=M or ddy>=N or ddx<0 or ddy<0: continue

            if maps[ddy][ddx]==1 and not visited[ddy][ddx]:     
                maps[ddy][ddx]=maps[y][x]+1       
                visited[y][x]=1
                q.append((ddy, ddx))

    return -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	))
# print(solution(	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
# print(solution([[1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1]] ))
# print(solution([[0]]))