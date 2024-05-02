n, k = map(int,input().split())
coin = [0]
for _ in range(n):
    coin.append(int(input()))

dp=[10101]*(k+1)
dp[0]=0
for i in range(1, n+1):
    for j in range( k+1):
        if j-coin[i]>=0: 
            dp[j] = min(dp[j], dp[j-coin[i]]+1)

if dp[k]==10101:
    print(-1)
else:
    print(dp[k])
