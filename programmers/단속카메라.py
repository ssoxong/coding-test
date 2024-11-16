def solution(routes):
    routes.sort()
    mins = routes[0][0]
    maxs = sorted(routes, key = lambda x:x[1])[-1][1]
    cam = 0
    cur = []
    cnt = 0

    s = mins
    e = routes[0][1]
    for r in routes:
        if r[0]<=e:
            cnt+=1
        if r[1]<e:
            e=r[1]
        if e<r[0]:
            cnt=1
            cam+=1
            e=r[1]
    return cam+1

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3],[1,1]]	))