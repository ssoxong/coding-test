def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    answer = 0 
    i=0
    for a in A:
        if a<B[i]:
            answer+=1
            i+=1
    return answer

# print(solution([2,2,2,2],	[1,1,1,9]))
print(solution([5,1,3,7]	,[2,2,6,8]))