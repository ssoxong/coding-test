n = int(input())
arr = list(map(int, input().split()))
ans = {x: 0 for x in arr}

index_map = {value: idx for idx, value in enumerate(arr)}

def switch(a, b):
    arr[a], arr[b] = arr[b], arr[a]
    index_map[arr[a]], index_map[arr[b]] = a, b

num = 1
for i in range(n):
    if arr[i] != num:
        target_idx = index_map[num]
        switch(i, target_idx)
        ans[arr[i]] += abs(i - target_idx)
        ans[arr[target_idx]] += abs(i - target_idx)
    num += 1 

result = [ans[key] for key in sorted(ans)]
print(*result)
