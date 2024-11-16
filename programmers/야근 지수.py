def solution(n, works):
    if sum(works) <= n:  # 모든 작업을 처리할 수 있는 경우
        return 0
        
    works.sort(reverse=True)  # 내림차순 정렬
    
    while n > 0:
        max_val = works[0]  # 현재 최대값
        
        # 최대값과 같은 요소들을 모두 1씩 감소
        for i in range(len(works)):
            if works[i] == max_val and n > 0:
                works[i] -= 1
                n -= 1
            else:
                break
                
        # 정렬 유지
        works.sort(reverse=True)
    
    return sum(w * w for w in works)

print(solution(99, [2, 15, 22, 55, 55]))
