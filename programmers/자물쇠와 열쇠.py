def solution(key, lock):
    n = len(lock)
    m = len(key)
    # lock 반대로
    llock = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                llock[i][j] = 1
            else: llock[i][j] = 0

    # padded key 생성
    padded_key = [[0 for _ in range(m+n*2-2)]for _ in range(m+n*2-2)]

    def check(pk, a, b):
        for i in range(n):
            for j in range(n):
                if pk[a+i][b+j]!=llock[i][j]: return False

        return True

    pm = len(padded_key)
    import copy
    kkey = copy.deepcopy(key)
    for _ in range(4):
        # key rotation
        for r in range(m):
            for c in range(m):
                key[c][m-1-r] = kkey[r][c]

        for a in range(m):
            for b in range(m):
                padded_key[a+n-1][b+n-1] = key[a][b]

                for i in range(0, pm-n+1):
                   for j in range(0, pm-n+1):
                        if check(padded_key, i, j): return True
        kkey = copy.deepcopy(key)

    return False

print(solution([[0, 0], [0, 0]], [[1, 0, 0], [1, 0, 0], [1, 1, 1]]))