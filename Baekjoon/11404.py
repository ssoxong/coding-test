def floyd(n, d, next):
    # 플로이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    next[i][j] = next[i][k]

def visited(u, v, next):
    # 경로를 재구성하는 함수
    if next[u][v] == None:
        return []  # 경로가 없는 경우

    path = [u]
    while u != v:
        u = next[u][v]
        path.append(u)
    return path

n = int(input())
m = int(input())

d = [[1e9] * (n + 1) for _ in range(n + 1)]
next = [[None] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    d[i][i] = 0

for _ in range(m):
    s, e, w = map(int, input().split())
    if d[s][e] > w:
        d[s][e] = w
        next[s][e] = e

floyd(n, d, next)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if d[i][j] >=1e9:
            print(0, end=" ")
        else:
            print(d[i][j], end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if d[i][j] == float('inf'):
            print(0)
        else:
            path = visited(i, j, next)
            print(len(path), *path)
