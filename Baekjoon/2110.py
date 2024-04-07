n, c = map(int,input().split())
xlist=[]
for _ in range(n):
    xlist.append(int(input()))

xlist.sort()

start = 1
end = xlist[-1]-xlist[0]
ans = 0
while(start<=end):
    mid = (start+end)//2
    x = xlist[0]
    cnt = 1

    for xi in xlist:
        if xi>=x+mid:
            cnt+=1
            x = xi
    if cnt>=c:
        start = mid+1
        ans = mid
    else:
        end = mid-1

print(ans)
