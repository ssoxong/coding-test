from itertools import permutations
import sys
input = sys.stdin.readline
def solution(n, arr, op):
    opl = []
    for i, o in enumerate(op):
        opl+=[i]*o

    amax, amin = -1e9, 1e9
    for p in permutations(opl, n-1):
        ans = arr[0]
        for i, a in enumerate(arr):
            if i==0: continue
            if p[i-1]==0:
                ans+=a
            elif p[i-1]==1:
                ans-=a
            elif p[i-1]==2:
                ans*=a
            elif p[i-1]==3:
                ans=int(ans/a)

        amax = max(ans, amax)
        amin = min(ans, amin)

    print(amax)
    print(amin)


solution(int(input()), list(map(int,input().strip().split())), list(map(int,input().strip().split())))