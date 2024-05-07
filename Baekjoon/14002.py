import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

dp = [1] * n
p = [-1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            p[i] = j

max_length = max(dp)
pos = dp.index(max_length)

ans = []
while pos != -1:
    ans.append(arr[pos])
    pos = p[pos]

ans.reverse()

print(max_length)
print(*ans)
