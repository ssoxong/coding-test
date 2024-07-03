import sys
input = sys.stdin.readline

n = int(input())
mone = -1
for x in range(n):
    card = list(map(int,input().split()))
    one = 0
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                one = (card[i] + card[j] + card[k]) % 10 # 일의 자리 수 구하기
                if one >= mone: # 제일 큰 수 구하기
                    mone = one
                    winner = x+1
print(winner)
