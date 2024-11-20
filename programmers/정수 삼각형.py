def solution(tri):
    dp = [[-1 for _ in range(len(x))]for x in tri]
    dp[0][0] = tri[0][0]
    
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            if j-1<0:
                dp[i][j] = max(dp[i][j], dp[i-1][j]+tri[i][j])
            elif  j==len(tri[i-1]): 
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+tri[i][j])
            else: 
                dp[i][j] = max(dp[i][j], dp[i-1][j]+tri[i][j], dp[i-1][j-1]+tri[i][j])
    
    return max(dp[len(tri)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))