def solution(blen, weight, tw):
    time = 0
    tmap = [[]for _ in range(len(tw))]
    for i, t in enumerate(tw):
        tmap[i] = [t, 0]

    cnt = 0 # 현재 다리에 있는 트럭 수
    totalw = 0 # 현재 다리에 있는 트럭의 총 무게
    curt = []

    i = 0
    while(i<len(tw)):
        # 가장 앞 트럭 나가기
        if cnt+1>blen or totalw+tw[i]>weight:
            cnt-=1
            totalw-=tw[curt[0]]
            ct = max(blen-tmap[curt[0]][1],0)
            # print(ct)
            time += ct
            tmap[curt.pop(0)][1]=-1
            for c in curt:
                tmap[c][1]+=ct

        # 트럭 삽입
        if totalw+tw[i]<=weight:
            cnt+=1
            totalw+=tw[i]
            curt.append(i)
            time+=1
            for c in curt:
                tmap[c][1]+=1

        else: i-=1
        i+=1
        print(time, tmap, curt)
    return time+blen

print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]		))
print(solution(2,10,[7,4,5,6]))
print(solution(100	,100	,[10]))
print(solution(	10, 100, [50, 30, 10, 10, 30, 10, 40]))