def solution(arr):
    answer = []
    size = len(arr)
    
    for i in range(size-1):
        if(arr[i]!=arr[i+1]):
            answer.append(arr[i])
        if(i==size-2):
            answer.append(arr[i+1])
            
    return answer