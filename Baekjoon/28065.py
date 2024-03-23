n = int(input())

for i in range(1, (n//2)+1):
    if n%2==0:
        print(n-i+1, end=" ")
        print(i, end=" ")
    else:
        print(n-i+1, end=" ")
        print(i, end=" ")
        if i==(n//2):
            print(i+1)