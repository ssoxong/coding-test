def solution(n, works):
    answer = 0
    i = 0
    works.sort(reverse=True)

    if sum(works)<=n: return 0
    
    while(n):
        works[i]-=1
        if i-1>=0 and works[i]<works[i-1]: i=i-1
        if i+1<len(works) and works[i]<works[i+1]: i=i+1
        n-=1

    for w in works:
        if w<0: continue
        answer+=w**2

    return answer

print(solution(99, [2, 15, 22, 55, 55]))
