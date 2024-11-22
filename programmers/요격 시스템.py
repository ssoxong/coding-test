def solution(targets):

    targets.sort(key=lambda x:(x[0],x[1]))
    # double targets
    dt = [[x*2+1, y*2-1] for x, y in targets]
    s, e = dt[0][0], dt[0][1]
    
    cnt = 0
    for a, b in dt:
        # print(s,e,a, b, cnt)
        # s, e 범위 안에 없으면 미사일 +=1
        if e<a:
            cnt+=1
            s, e = a, b
        else: 
            if s<=a<=e:
                s = max(s, a)
            if s<=b<=e:
                e = min(e, b)
    return cnt+1

print(solution([[0, 4], [0, 1], [2, 3]] ))