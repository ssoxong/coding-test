import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 1
        elif arr[mid]>target:
            end = mid-1
        elif arr[mid]<target:
            start = mid+1
    return 0

for a in arr2:
    print(binary_search(arr, a))
