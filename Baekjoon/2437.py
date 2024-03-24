import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

k = 1

for a in arr:
    if k < a:
        break

    k += a

print(k)