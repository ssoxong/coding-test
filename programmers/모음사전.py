from itertools import product
def solution(word):
    mlist = ['A','E','I','O','U']
    com = []
    for i in range(1, 6):
        cc = product(mlist, repeat=i)
        for c in cc:
            com.append("".join(c))
    com.sort()
    return com.index(word)+1

print(solution("EIO"))