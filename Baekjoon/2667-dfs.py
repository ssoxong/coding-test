import sys
input = sys.stdin.readline
n = int(input())
maze = [list(map(int, input().strip())) for _ in range(n)]

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 상하좌우

def dfs(a, b):
    print(maze[a][b])
   
    maze[a][b] = -1

    for dy, dx in move:
        ny, nx = a + dy, b + dx
        # 범위 밖을 벗어나지 않으면서 1이 아니고, 방문하지 않았을 경우
        if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] != 1 :
            dfs(ny, nx)


N = 5
print(dfs(0,3))
