import heapq

def solution(jobs):
    jj = []

    cur_time = 0
    ans = []
    start = -1
    while(len(ans)<len(jobs)):
        for j in jobs:
            if start<j[0]<=cur_time:
                # 소요시간 요청시간
                heapq.heappush(jj,(j[1], j[0]))
        
        if not len(jj): cur_time+=1; continue

        h = heapq.heappop(jj)
        start = cur_time
        cur_time+=h[0]
        # print(cur_time, h[1])
        ans.append(cur_time-h[1])
        
    # print(ans)
    return sum(ans)//len(ans)

# print(solution([[0, 5], [2, 10], [10000, 2]]	))
print(solution(	[[0, 3], [1, 9], [2, 6]]))