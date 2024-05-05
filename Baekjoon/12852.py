import sys
input = sys.stdin.readline
n = int(input())
dp=[0]*1000001
num=[-1]*1000001
dp[1]=0
num[1]=-1


for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    num[i] = i-1
    if i%2==0:
        if dp[i]>dp[i//2]+1:
            dp[i] = dp[i//2]+1
            num[i]=i//2
    if i%3==0:
        if dp[i]>dp[i//3]+1:
            dp[i] = dp[i//3]+1
            num[i]=i//3
print(dp[n])
i = n
while i!=-1:
    print(i, end=' ')
    i=num[i]