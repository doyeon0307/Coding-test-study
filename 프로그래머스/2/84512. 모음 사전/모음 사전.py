def get_idx(c):
    if c == 'A':
        return 0
    if c == 'E':
        return 1
    if c == 'I':
        return 2
    if c == 'O':
        return 3
    if c == 'U':
        return 4

def solution(word):
    answer = 1
    
    alphabet = ['A', 'E', 'I', 'O', 'U']
    w = 'A'
    
    while w != word:
        print(w)
        answer += 1
        
        # 5자리가 아니면 뒤에 A 추가
        if len(w) < 5:
            w += 'A'
            continue
        
        # 맨 마지막 알파벳 구하기
        idx = get_idx(w[-1])
        
        # 마지막이 U가 아니면 > 그 다음 알파벳으로 변경
        if idx < 4:
            w = w[:4] + alphabet[idx + 1]
        # 마지막이 U면 > 맨 뒤에서부터 U가 아닌 거 이전을 다음 알파벳으로 변경
        # e.g.AAUUU > AE
        else:
            change_idx = 4
            while change_idx > 0 and w[change_idx] == 'U':
                change_idx -= 1
            if change_idx == 0:
                w = alphabet[get_idx(w[change_idx]) + 1]
            else:
                w = w[:change_idx] + alphabet[get_idx(w[change_idx]) + 1]
            
    return answer