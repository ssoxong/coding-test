def solution(diffs, times, limit):
    answer = 0
    start = 1
    end = 100000
    total_spend = 0

    while(start<=end):
        level = (start+end)//2

        total_spend = 0
        spend = 0
        time_prev = 0

        for i, d in enumerate(diffs):
            if d <= level:
                spend = times[i]
            else:
                spend =(times[i]+time_prev)*(d-level)+times[i]

            time_prev = times[i]
            total_spend+=spend

        if total_spend<=limit: 
            end = level-1
        else:
            start = level+1

    return start

diffs, times, limit = [1, 5, 3], [2, 4, 7], 30

print(solution(diffs, times, limit))