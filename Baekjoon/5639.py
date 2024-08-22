import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution():
    nodes = []
    while True:
        try:
            nodes.append(int(input().strip()))
        except:
            break
 
    def pre_to_post(nodes):
        if len(nodes)==0: return

        root = nodes[0]
        lv, rv = [], []
        for i in range(1,len(nodes)):
            if nodes[i]>root:
                lv = nodes[1:i]
                rv = nodes[i:]
                break
            if i==len(nodes)-1:
                lv = nodes[1:]
        
        pre_to_post(lv)
        pre_to_post(rv)
        print(root)

    pre_to_post(nodes)

solution()