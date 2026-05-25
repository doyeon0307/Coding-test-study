def solution(participant, completion):
    answer = ''
    
    name = {}
    
    for p in participant:
        name[p] = name.get(p, 0) + 1
    
    for c in completion:
        name[c] -= 1
        
    for i in name.items():
        if i[1] > 0:
            return i[0]
    
    return answer