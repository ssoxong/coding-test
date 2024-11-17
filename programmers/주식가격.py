def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(answer)):
        answer[i] = len(prices)-i-1

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[i]>prices[j]:
                answer[i] = j-i
                break
    return answer

print(solution([1,2,3,2,3]))