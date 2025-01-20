def solution(stones, k):
    first = 1
    second = 200000000

    while(first<second):
        hole = 0
        mid = (first+second)//2
        for s in stones:
            if s-mid<=0:
                hole+=1
            else: 
                hole=0
            if hole>=k: break

        if hole>=k:
            second = mid-1
        else:
            first = mid+1

    return first

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))