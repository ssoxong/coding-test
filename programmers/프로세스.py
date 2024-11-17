def solution(p, l):
    loc = []
    cnt=1
    for i in range(len(p)):
        loc.append((p[i], i))

    i=0
    while(1):
        if any(loc[i][0]<l[0] for l in loc) or loc[i][0]==-1: i=(i+1)%len(p); continue
        if loc[i][1]==l: return cnt
        loc[i] = (-1, -1)
        cnt+=1

        

print(solution([1, 1, 9, 1, 1, 1]	, 0))
    
