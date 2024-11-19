def solution(sizes):
    w = []
    h = []
    for s in sizes:
        if s[0]<s[1]:
            w.append(s[0])
            h.append(s[1])
        else:
            w.append(s[1])
            h.append(s[0])
    return max(w)*max(h)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))