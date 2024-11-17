def solution(a):
    answer = 0
    left, right = a[0], min(a[1:])
    dp = [[0 for _ in range(len(a))] for _ in range(2)]
    dp[0][0] = a[0]
    dp[1][-1] = a[-1]
    for i in range(1, len(a)):
        dp[0][i] = min(dp[0][i-1],a[i])
    for i in range(len(a)-2, -1, -1):
        dp[1][i] = min(dp[1][i+1],a[i])
    
    for i in range(1,len(a)-1):
        last = a[i]
        left = dp[0][i-1]
        right = dp[1][i+1]
        if (left>last or right>last):answer+=1

    return answer+2

print(solution([100,1,2,101]))