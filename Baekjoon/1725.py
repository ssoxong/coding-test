import sys
input = sys.stdin.readline

n = int(input())
narr = []
for _ in range(n):
    narr.append(int(input()))

def histogram(nlist, start, end):
    if start>end: return 0
    if start==end: return nlist[start]
    mid = (start+end)//2
    res = nlist[mid]
    cnt = 1
    mn = nlist[mid]
    i = mid-1
    j = mid+1

    while start <= i and j<=end:
        if nlist[i]>nlist[j]:
            cnt+=1
            mn = min(mn, nlist[i])
            i-=1
        else:
            cnt+=1
            mn = min(mn, nlist[j])
            j+=1
        res = max(res, cnt*mn)

    while start<=i:
        cnt+=1
        mn = min(mn, nlist[i])
        i-=1
        res = max(res, cnt*mn)
    while j<=end:
        cnt+=1
        mn = min(mn, nlist[j])
        j+=1
        res = max(res, cnt*mn)
    res = max(res, histogram(nlist, start, mid-1))
    res = max(res, histogram(nlist, mid+1, end))
    
    return res

res = histogram(narr, 0, n-1)
print(res)
