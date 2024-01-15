def solution(clothes):
    answer = 1
    arr={}
    
    for cloth in clothes:
        if cloth[1] not in arr.keys():
            arr[cloth[1]]=1
        else:
            arr[cloth[1]]+=1
    
    for _, a in arr.items():
        answer*=(a+1)
        
    answer-=1
    return answer