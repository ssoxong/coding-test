import sys
input = sys.stdin.readline

n = int(input())

endPoint = 0
ans = 0

arr = []

for i in range(0,n):
    a, b = map(int,input().rstrip().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

for start, end in arr:
    if endPoint <= start:
        ans += 1
        endPoint = end
print(ans)