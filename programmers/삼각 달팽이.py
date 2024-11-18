def solution(n):
    tra = [[0 for j in range(1, i+1)] for i in range(1, n+1) ]
    y,x = -1,0
    cnt = 1
    answer = []

    for i in range(n):
        for _ in range(i,n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            else:
                x -= 1
                y -= 1

            tra[y][x] = cnt
            cnt += 1
    for t in tra:       
        answer+=t
        
    return answer

print(solution(4))