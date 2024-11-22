def solution(routes):
    routes.sort(key=lambda x:x[1])
    e = routes[0][1]

    cam = 0
    for a, b in routes:
        if e<a:
            e=b
            cam+=1

    return cam+1

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	))