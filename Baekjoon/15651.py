from itertools import product
def solution(n, m):
    num = [x for x in range(1, n+1)]
    pp = product(num,repeat=m )
    for p in pp:
        print(*p)

n, k = map(int, input().split())
solution(n, k)