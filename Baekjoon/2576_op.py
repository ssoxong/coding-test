from collections import deque

# 가로 세로
def solution(m,n,arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                q.append((j, i))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not(0<=nx<m and 0<=ny<n): continue
            if arr[ny][nx]==0:
                q.append((nx, ny))
                arr[ny][nx]=arr[y][x]+1
    
    for ar in arr:
        if ar.count(0)>0: print(-1); exit(0) 
    ans = 0
    for ar in arr:
        ans = max(ans, max(ar))

    print(ans-1)

if __name__=="__main__":
    m, n = map(int,input().split())
    arr = [[]for _ in range(n)]
    for i in range(n):
        arr[i]=list(map(int,input().split()))
    solution(m,n,arr)