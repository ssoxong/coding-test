def solution(n, times):
    s = 1
    e = n*max(times)
    ans = 0
    while(s<=e):
        mid = (s+e)//2
        print(s, e, mid)

        nn = sum(mid//time for time in times)
        # 시간 늘리기
        if nn<n:
            s = mid+1
        # 시간 줄이기
        elif nn>=n:
            ans = mid
            e = mid-1
    return ans

print(solution(6, [7,10,9]))