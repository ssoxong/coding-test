import sys
input = sys.stdin.readline

n = int(input())

stars = [[' ']*2*n for _ in range(n)]

def rec(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"
    
    else:
        rec(i, j, size//2)
        rec(i + size//2, j - size//2, size//2)
        rec(i + size//2, j + size//2, size//2)

rec(0, n - 1, n)
for star in stars:
    print("".join(star))