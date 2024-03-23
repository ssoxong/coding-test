n = int(input())

ans = 0
arr =[[0,0]]
def hanoi(n, a, b, c):
    global ans
    
    if n==1:
        ans+=1
        arr.append([a,c])
        return
    hanoi(n-1, a, c, b)
    hanoi(1, a, b, c)
    hanoi(n-1, b, a, c)

hanoi(n, 1, 2, 3)

print(ans)
for a in arr[1:]:
    print(a[0], a[1])