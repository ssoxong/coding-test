import heapq
def solution(scoville, k):
    cnt = 0
    make = 0
    heapq.heapify(scoville)
    if scoville[0]>=k: return cnt
    while(len(scoville)>1):
        make = heapq.heappop(scoville)+heapq.heappop(scoville)*2
        heapq.heappush(scoville, make)
        cnt+=1
        if scoville[0]>=k: return cnt

    return -1


# print(solution([1, 2, 3, 9, 10, 12],	7))
# print(solution([1,1],5))
print(solution([3,4,5,6,7],10))
print(solution([7,6,5,4,3],10))

# print(solution([1,2,3],45))