n = int(input())
arr = [[0]*n for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,(list(input()))))

stack = []
def isOk(size, x, y):
    first = arr[y][x]
    for dx in range(x, x+size):
        for dy in range(y, y+size):
            if arr[dy][dx]!=first:
                return False
    stack.append(first)
    return True

def press(size, x, y):
    if isOk(size, x, y):
        return
    
    stack.append('(')
    press(size//2, x, y)
    press(size//2, x+size//2, y)
    press(size//2, x, y+size//2)
    press(size//2, x+size//2, y+size//2)

    stack.append(')')
    

press(n, 0, 0)
for s in stack:
    print(s,end="")