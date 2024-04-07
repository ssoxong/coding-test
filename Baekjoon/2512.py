n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
start, end = 0, max(nlist)

while start <= end:
    mid = (start+end) // 2
    total = 0
    for i in nlist:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid + 1
    else: 
        end = mid - 1
print(end)