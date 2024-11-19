def solution(routes):
    routes.sort()
    s, e = routes[0]

    cam = 0

    for r in routes:
        # print(r, s, e, cam)?
        if s<=r[0] and r[0]<=e:
            s = max(s, r[0])
            e = min(e, r[1])
        else:
            cam+=1
            s, e = r

    return cam+1

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	))