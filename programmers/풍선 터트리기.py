def solution(arr):
    ma = [[x for x in arr], [x for x in arr[::-1]]]
    for i in range(1, len(arr)):
        ma[0][i]=min(ma[0][i], ma[0][i-1])
    for i in range(1, len(arr)):
        ma[1][i]=min(ma[1][i], ma[1][i-1])
    ma[1] = ma[1][::-1]
    # print(ma)
        
    cnt = 0
    for i in range(len(arr)):
        if ma[0][i]>=arr[i] or ma[1][i]>=arr[i]:
            cnt+=1
        
    return cnt