n, m = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(m):
    i, a, b = map(int,input().split())
    if i==1:
        arr[a-1]=b
    elif i==2:
        for j in range(a-1, b):
            arr[j]= not arr[j]
    elif i==3:
        for j in range(a-1, b):
            arr[j]= 0
    elif i==4:
        for j in range(a-1, b):
            arr[j]= 1

for a in arr:
    if(a or a==1):
        print(1, end=" ")
    else:
        print(0, end=" ")