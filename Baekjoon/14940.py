# 쉬운 최단거리
# BFS
from collections import deque

def solution(n, m, arr):
    global distance
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    u, v = 0, 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작점 찾기
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j]==2:
                u, v = j, i
                break
    
    distance[v][u] = 0
    q.append((u, v))
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<len(arr[0]) and 0<=ny<len(arr):
                if arr[ny][nx]==1 and distance[ny][nx]==-1:
                    distance[ny][nx] = distance[y][x]+1
                    q.append((nx, ny))

if __name__=="__main__":
    n, m = map(int,input().split())
    arr = [[]for _ in range(n)]
    distance=[[]]

    for i in range(n):
        arr[i] = list(map(int,input().split()))

    solution(n, m, arr)

    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                print(0, end=' ')
            else:
                print(distance[i][j], end=' ')
        print()