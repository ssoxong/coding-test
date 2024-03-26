n, a, b = map(int,input().split())
cnt = 0

def press(size, x, y):
    global cnt
    if size==1:
        if x==a and y==b:
            print(cnt)
            exit(0)
        # arr[x][y] = cnt
        cnt+=1
        return
    
    if x<=a and a<x+(size//2)+1 and y<=b and b<y+(size//2)+1:
        press(size//2, x, y)
    else:
        cnt+=pow((size//2),2)

    if x<=a and a<x+(size//2)+1 and y+size//2<=b and b<y+size+1:
        press(size//2, x, y+size//2)
    else:
        cnt+=pow((size//2),2)

    if x+size//2<=a and a<x+size+1 and y<=b and b<y+(size//2)+1:
        press(size//2, x+size//2, y)
    else:
        cnt+=pow((size//2),2)

    if x+size//2<=a and a<x+size+1 and y+size//2<=b and b<y+size+1:
        press(size//2, x+size//2, y+size//2)
    else:
        cnt+=pow((size//2),2)


press(pow(2,n), 0, 0)
