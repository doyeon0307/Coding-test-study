from itertools import permutations

def go(cnt, power, i, dungeons):
    if dungeons[i][0] > power:
        return cnt, power
    return cnt + 1, power - dungeons[i][1]

def solution(k, dungeons):
    answer = -1
    
    n = len(dungeons)
    idxs = [i for i in range(n)]
    
    perm = list(permutations(idxs, n))
    
    for p in perm:
        cnt = 0
        power = k
        for i in p:
            cnt, power = go(cnt, power, i, dungeons)
        answer = max(cnt, answer)
    
    return answer