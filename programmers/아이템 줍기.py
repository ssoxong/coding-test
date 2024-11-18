import time

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    cx*=2; cy*=2; ix*=2; iy*=2
    ccx = cx
    ccy = cx
    n = 10
    pan = [[-1 for _ in range(n*2+1)] for _ in range(n*2+1)]
    visited = [[0 for _ in range(n*2+1)] for _ in range(n*2+1)]
    for r in rectangle:
        sx, sy, ex, ey = r
        sx*=2; sy*=2; ex*=2; ey*=2
        for i in range(sy, ey+1,2):
            for j in range(sx, ex+1,2):
                pan[i][j] = 1
                pan[i][j+1] = 1
                pan[i+1][j] = 1
                pan[i+1][j+1] = 1
    tmp = []


    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(1, n*2+1):
        for j in range(1, n*2+1):
            if pan[i][j]!=1: continue
            tt = True
            for ddx in dx:
                for ddy in dx:
                    if pan[i+ddy][j+ddx]!=1: tt = False
            
            if tt: tmp.append((i, j))

    for y, x in tmp:
        pan[y][x] = 0

    for p in pan:
        print(p)

    visited[cy][cx]=1
    ans = []
    dis = 0
    while(1):
        # print(cy, cx)
        # time.sleep(1)
        for i in range(4):
            # print(cy, cx, visited[cy+dy[i]][cx+dx[i]], pan[cy+dy[i]][cx+dx[i]])
            if not visited[cy+dy[i]][cx+dx[i]] and pan[cy+dy[i]][cx+dx[i]]==1:
                dis+=1
                visited[cy+dy[i]][cx+dx[i]]=1

                cx+=dx[i]
                cy+=dy[i]

                print(cy, cx, iy, ix)

                if cx==ix and cy==iy:
                    ans.append(dis)
                    print(ans)
                    if len(ans)==2: 
                        print(ans)
                        return ans
                    cx = ccx
                    cy = ccy
                    dis = 0
                    break

                continue
        
    

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],	1,	3,	7,	8))