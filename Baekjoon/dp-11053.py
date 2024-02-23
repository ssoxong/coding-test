import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = [0]*(len(arr))


def rec(a):
    if dp[a]!=0:
        return dp[a]
    maxArr = []
    for i in range(a, len(arr)):
        if arr[i]>arr[a]:
            maxArr.append(i)
    
    if len(maxArr)==0:
        dp[a]=1
        return 1
    else:
        dp[a]=1+max([rec(i) for i in maxArr])
        return dp[a]
    
for i in range(n):
    rec(i)
print(max(dp))