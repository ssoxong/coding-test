n, m = map(int,input().split())
arr = [[0]*m for _ in range(n)]

for i in range(m):
    tarr=(list(map(int, input().split())))
    for j in range(n):
        arr[j][i] = tarr[j]

for i in range(n):
    arr[i].sort()


mid = [0]*n
if m%2==0:
    for i in range(n):
        mid[i] = (arr[i][m//2]+arr[i][(m//2)-1])//2
else:
    for i in range(n):
        mid[i] = arr[i][m//2]

sum = 0

for j in range(m):
    for i in range(n):
        sum += abs(arr[i][j]-mid[i])
    
print(sum)

for m in mid:
    print(m, end=' ')