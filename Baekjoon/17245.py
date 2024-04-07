n = int(input())
nlist = []
for _ in range(n):
    nlist += list(map(int, input().split()))

total = sum(nlist)
ans = 0
start = 0
end = max(nlist)
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for nl in nlist:
        sum += nl if nl < mid else mid

    if sum < total / 2:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
print(ans)