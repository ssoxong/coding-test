import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nlist = list(map(int,input().split()))
arr = [0]

sum = 0
for i in nlist:
    sum+=i
    arr.append(sum)
# print(arr)

for _ in range(m):
    i, j = map(int,input().split())
    print(arr[j]-arr[i-1])
