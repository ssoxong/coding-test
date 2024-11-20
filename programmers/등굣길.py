def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1) ]for _ in range(n+1)]
    dp[1][1]=1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i==1 and j==1: continue
            if [i, j] in puddles:
                dp[j][i] = 0
            else:
                dp[j][i] = (dp[j-1][i]+dp[j][i-1])%1000000007
    return dp[n][m]

print(solution(4,3,[[2,1]]))