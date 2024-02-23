import sys
input = sys.stdin.readline

move = [[1,0],[0,1],[-1,0],[0,-1]]
count = 0

def bfs(y,x):
    queue = []
    queue.append([y,x])

    while queue: 
        dy, dx = queue.pop(0)

        if field[dy][dx]== 0:
            continue

        field[dy][dx]=0

        for mo in move:
            ny = dy+mo[0]
            nx = dx+mo[1]
            if ny<n and nx<m and ny>=0 and nx>=0 and field[ny][nx]==1:
                queue.append([ny,nx])
        

t = int(input())
for _ in range(t):
    count = 0
    m, n, k = map(int,input().split())
    field = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int,input().split())
        field[y][x] = 1


    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                bfs(i,j)
                count+=1

    print(count)