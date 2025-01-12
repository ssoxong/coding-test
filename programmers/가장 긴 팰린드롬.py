def solution(s):
    answer = 1
    for i in range(1, len(s)):
        for j in range(1, len(s)):
            if i+j>=len(s) or i-j<0: break
            if s[i-j]==s[i+j]: 
                answer = max(answer, j*2+1)
            else: break    
    for i in range(0, len(s)):
        for j in range(1, len(s)):
            if i+j>=len(s) or i-j+1<0: break
            if s[i-j+1]==s[i+j]: 
                answer = max(answer, j*2)
            else: break    
    return answer

print(solution("abba"))