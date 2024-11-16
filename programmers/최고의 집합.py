def solution(n, s):
    answer = []
    for _ in range(n):
        answer.append(s//n)
    for i in range(s%n):
        answer[i]+=1
    if s<n: return [-1]
    return sorted(answer)

print(solution(4,4))