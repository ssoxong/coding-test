import sys
sys.setrecursionlimit(10**9)

n = int(input())
arr = list(map(int, input().split()))
fruits = [0] * 10

def find(start, end, max_fruits, kind):
    global n
    if end >= n:
        return max_fruits
    
    fruits[arr[end]] += 1
    if fruits[arr[end]] == 1:
        kind += 1
        
    if kind > 2:
        fruits[arr[start]] -= 1
        if fruits[arr[start]] == 0:
            kind -= 1
        start += 1
    
    max_fruits = max(max_fruits, end - start + 1)
    return find(start, end+1, max_fruits, kind)
    
print(find(0, 0, 0, 0))