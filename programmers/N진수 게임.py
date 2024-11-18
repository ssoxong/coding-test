def translation(n, t, m, p):
    s = '0'
    for i in range(t*m+p):
        # if (t*m+p)<len(s): break

        tmps = ''
        if i==0: tmps='0'
        while(i>0):
            i, mod = divmod(i, n)
            if mod%10!=mod:
                mod = chr(ord('A')+mod%10)
            tmps+=str(mod)

        s+=tmps[::-1]

    return s

def solution(n, t, m, p):
    s = translation(n, t, m, p)
    ans = ''
    for i in range(t):
        ans+=s[i*m+p]
    return ans

print(solution(16,16,2,1))