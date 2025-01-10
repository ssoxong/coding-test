def solution(cookie):
    answer = 0
    
    hap = [0 for _ in range(len(cookie))]
    hap[0] = cookie[0]
    for i, c in enumerate(cookie):
        if i==0: continue
        hap[i]=hap[i-1]+c

    for m in range(len(cookie)):
        left, right = 0, len(cookie)-1
        while(left<right):
            if left==0: first = hap[m]
            else: first = hap[m]-hap[left-1]
            second = hap[right]-hap[m]
            if first==second: answer = max(answer, first); break
            elif first<second: right-=1
            elif first>second: left+=1
    return answer

cookie = [1,1,2,3]
print(solution(cookie)) # 3