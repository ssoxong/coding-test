def solution(p, s):
    answer = []
    while(p):
        print(p)
        day = (100-p[0])//s[0]
        if (100-p[0])%s[0]!=0: day+=1

        for i in range(len(p)):
            p[i]+=s[i]*day

        cnt = 0
        while(1 and len(p)):
            if p[0]<100: break
            p.pop(0)
            s.pop(0)
            cnt+=1
        answer.append(cnt)

    return answer

print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]
))