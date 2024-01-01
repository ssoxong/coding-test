import heapq

def solution(scoville, K):
    answer = 0
    isK = False
    heapq.heapify(scoville)

    while(not isK):
        for s in scoville:
            if not s>=K:
                break
            elif s==scoville[-1]:
                return answer

        if len(scoville)==1:
            return -1
        
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville,f+s*2)
        
        answer+=1
    return answer