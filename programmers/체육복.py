def solution(n, lost, reserve):
    answer = 0
    have = [1 for _ in range(n)]
    for r in reserve:
        have[r-1]+=1
    
    for l in lost:
        have[l-1]-=1
        
        
    for index, h in enumerate(have):
        if(h==0):
            if(index!=0 and have[index-1]>1):
                have[index-1]-=1
                have[index]=1
            elif (index!=n-1 and have[index+1]>1):
                have[index+1]-=1
                have[index]=1  
    
    for h in have:
        if(h!=0):
            answer+=1
    return answer