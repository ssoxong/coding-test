import sys
input = sys.stdin.readline

t = int(input())
dp = [0]*101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9

def rec(n):
    if dp[n]!=0:
        return dp[n]
    
    dp[n] = rec(n-1)+rec(n-5)


for _ in range(t):
    n = int(input())
    for i in range(10, n+1):
        dp[i] = rec(i-1)+rec(i-5)
    print(dp[n])


