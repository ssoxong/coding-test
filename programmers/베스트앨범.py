def solution(genres, plays):
    answer = []
    mmap = {}
    for i in range(len(genres)):
        if genres[i] not in mmap:
            mmap[genres[i]]=[]
        mmap[genres[i]].append((plays[i], i))

    total = {}
    for m in mmap.keys():
        total[m]=0
        mmap[m].sort(key=lambda x: (-x[0], x[1]))
        for p, i in mmap[m]:
            total[m]+=p

    for k, t in sorted(total.items(), key=lambda x: -x[1]):
        for a in range(min(2, len(mmap[k]))):
            answer.append(mmap[k][a][1])
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"]	, [500, 600, 150, 800, 2500]	))