n = int(input())

fib = [0]*91
fib[0] = 0
fib[1] = 1
fib[2] = 1

for i in range(3, n+1):
    fib[i] = fib[i-1]+fib[i-2]

print(fib[n])