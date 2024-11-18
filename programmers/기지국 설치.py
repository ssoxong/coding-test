def solution(n, s, w):
    answer = 0

    no = []
    for i in range(len(s)-1):
        no.append(s[i+1]-w-1+1 - (s[i]+w+1))
    no.append(s[0]-w-1)
    if not s[-1]-w<=n<=s[-1]+w: 
        no.append(n-(s[-1]+w))

    print(no)
    for nno in no:
        answer+=nno//((w*2)+1)
        if nno%((w*2)+1)!=0: answer+=1
    
    return answer

# print(solution(11,	[4, 11],	1))
print(solution(16, [9],2))