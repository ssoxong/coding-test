import sys
input = sys.stdin.readline 

n, m = map(int,input().strip().split())
arr = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
exalpha = set(arr[0][0])

def dfs(a, b, count):
    global cnt  # 전역 변수를 사용한다고 명시
    cnt = max(cnt, count)

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] not in exalpha:
            exalpha.add(arr[nx][ny])
            dfs(nx, ny, count + 1)
            exalpha.remove(arr[nx][ny])

dfs(0, 0, 1)
print(cnt)
