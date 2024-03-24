import sys
input = sys.stdin.readline

n, k = map(int,input().split())
str = input().strip()
arr = [0]*(len(str)+1)
sum = 0
for index, s in enumerate(str, start=1):
    if s=='R':
        sum+=k
        arr[index] = sum
    elif s=='O':
        sum-=1
        arr[index]=sum

hmap = {}
for i, v in enumerate(arr):
    if v in hmap:
        hmap[v][1] = i
    else:
        hmap[v] = [i, i]

ans = 0
for imin, imax in hmap.values():
    ans = max(ans, imax - imin)

print(ans)