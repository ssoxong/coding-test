n = int(input())
alist = list(map(int,input().split()))

def gcd(a, b):
    if b:
        return gcd(b, a%b)
    else:
        return a

def gcdarr(arr):
	a = arr[0]
	for b in arr[1:]:
		a = gcd(a, b)
	return a
	

def binary_search(arr):
	mid = len(arr) // 2
	if len(arr) == 1:
		return arr[0]
	elif len(arr) == 2:
		return arr[0] + arr[1]
	
	return max(binary_search(arr[:mid]) + gcdarr(arr[mid:]), gcdarr(arr[:mid])+binary_search(arr[mid:]))
 
mid = n//2
if n == 1:
	print(alist[0])
else:
	print(max(binary_search(alist[:mid]) + gcdarr(alist[mid:]), gcdarr(alist[:mid])+binary_search(alist[mid:])))