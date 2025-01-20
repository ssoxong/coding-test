def solution(scores):
    tt = scores[0]

    scores.sort(key=lambda x:(-x[0], x[1]))        
    rank = 1
    tmp = 0
    for score in scores:
        if tt[0] < score[0] and tt[1] < score[1]:
            return -1

        if sum(tt) < sum(score) and tmp <= score[1]:
            rank += 1
            tmp = score[1]

    return rank