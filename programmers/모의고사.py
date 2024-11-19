def solution(answers):
    s = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

    dic = [[1, 0], [2, 0], [3, 0]]

    for i, a in enumerate(answers):
        s0i = i%len(s[0])
        s1i = i%len(s[1])
        s2i = i%len(s[2])

        if s[0][s0i]==a: dic[0][1]+=1
        if s[1][s1i]==a: dic[1][1]+=1
        if s[2][s2i]==a: dic[2][1]+=1
        
    dic.sort(key=lambda x:(x[0], x[1]))
    mmax = max(dic, key=lambda x: x[1])
    ans = []
    for d in dic:
        if d[1]!=mmax[1]: continue
        ans.append(d[0])
    return ans



print(solution([1,3,2,4,2]	))

