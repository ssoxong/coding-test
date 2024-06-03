import sys
input = sys.stdin.readline

n, k = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
ans=0
dp = {0:1}
s=0
for a in arr:
    s +=a
    if s-k in dp.keys():
        ans+=dp[s-k]
    dp[s] = dp.get(s, 0)+1
print(ans)
