from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i])!=len(banned_id[i]): return False

        for j in range(len(users[i])):
            if banned_id[i][j]=='*': continue
            if banned_id[i][j]!=users[i][j]: return False

    return True

def solution(user_id, banned_id):
    answer = 0

    per = list(permutations(user_id, len(banned_id)))
    ban = []

    for p in per:
        if not check(p, banned_id): continue
        p = set(p)
        if p not in ban:
            ban.append(p)

    answer = len(ban)
    return answer

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

solution(user_id, banned_id)
