n, k = map(int, input().split())
arr = list(map(int,input().split()))

def bubble():
    global k, arr
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if k==0: return
            if arr[j]>arr[j+1]:
                k-=1
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubble()

if k>0: print('-1')
else: print(*arr)
