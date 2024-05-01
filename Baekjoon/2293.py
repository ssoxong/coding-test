n, k = map(int,input().split())
coin = [0]
for _ in range(n):
    coin.append(int(input()))

dp=[0]*10101
dp[0]=1
for i in range(1, n+1):
    for j in range(1, k+1):
        if j-coin[i]>=0: dp[j]+=dp[j-coin[i]]

print(dp[k])