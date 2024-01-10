
from collections import deque

def bfs(x,y):
    global dx, dy, arr
    loc=deque()
    loc.append((x-1,y-1))
    arr[x-1][y-1]=1
    
    while loc:
        a, b = loc.popleft()

        for i in range(4):
            tmp_x = a+dx[i]
            tmp_y = b+dy[i]
            if tmp_x>=n or tmp_y>=n or tmp_x<0 or tmp_y<0:
                continue
            
            if arr[tmp_x][tmp_y]!=0:
                continue

            loc.append((tmp_x, tmp_y))
            arr[tmp_x][tmp_y] = arr[a][b]+1


n = int(input())
x, y = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

bfs(x,y)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()