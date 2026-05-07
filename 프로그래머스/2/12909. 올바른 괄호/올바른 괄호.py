def solution(s):
    answer = True
    
    cnt = 0
    
    for a in s:
        if a == "(":
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else:
                answer = False

    if not answer:
        return answer
    return cnt == 0