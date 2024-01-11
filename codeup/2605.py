
from collections import deque

def bfs(x,y):
    global dx, dy, arr, ans
    loc=deque()
    loc.append((x,y))

    color = arr[x][y]
    visited = [[False for _ in range(7)]*7]
    
    while loc:
        a, b = loc.popleft()
        visited[a][b]=True
        cnt = 0

        for i in range(4):
            tmp_x = a+dx[i]
            tmp_y = b+dy[i]W
            if(visited[tmp_x][tmp_y]):
                continue
            if tmp_x>=7 or tmp_y>=7 or tmp_x<0 or tmp_y<0:
                continue
            
            if arr[tmp_x][tmp_y]!=color:
                continue

            loc.append((tmp_x, tmp_y))
            cnt+=1

        if cnt==0:



arr = [[input() for _ in range(7)] for _ in range(7)]

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]
ans=0

bfs(0,0)

print(ans)