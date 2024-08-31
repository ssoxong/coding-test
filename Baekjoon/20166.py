import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, k = map(int,input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(n)]
kk = [input().rstrip() for _ in range(k)]

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 0, 0, -1, 1]
dic = {}

for target in kk:
    dic[target]=0

def dfs(x, y, s):
    if s in kk:
        dic[s]+=1
        return
    if len(s)>5:
        return
    
    for i in range(8):
        nx, ny = (x+dx[i])%m, (y+dy[i])%n
        dfs(nx, ny, s+arr[ny][nx])

# for target in kk:
#     if target in dic:
#         print(dic[target])
#         continue
#     else:
#         dic[target]=0
    
#     for i in range(0, n):
#         for j in range(0, m):
#             dfs(j, i, arr[i][j], target)
#     print(dic[target])

for i in range(0, n):
    for j in range(0, m):
        dfs(j, i, arr[i][j])

for d in dic:
    print(dic[d])