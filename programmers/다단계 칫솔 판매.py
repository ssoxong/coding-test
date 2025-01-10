def solution(enroll, referral, seller, amount):
    answer = []
    tree = {}
    
    for e, r in zip(enroll, referral):
        tree[e]=[r,0]
    for s, a in zip(seller, amount):
        money = a*100
        cur = s
        if money*0.1<1: tree[cur][1] += money
        else: tree[cur][1]+=money-int(money*0.1)

        while tree[cur][0]!='-':
            money=int(money*0.1)
            cur = tree[cur][0]
            if money*0.1<1: tree[cur][1] += money; break
            else: tree[cur][1]+=money-int(money*0.1)     

    return [x[1] for x in tree.values()]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	
seller = ["young", "john", "tod", "emily", "mary"]	
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))