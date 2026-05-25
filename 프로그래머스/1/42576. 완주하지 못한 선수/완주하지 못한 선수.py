def solution(participant, completion):
    answer = ''
    
    name = {}
    
    for p in participant:
        if p in name:
            name[p] += 1
        else:
            name[p] = 1
    
    for c in completion:
        if c in name:
            name[c] -= 1
            if name[c] <= 0:
                del name[c]
    
    return list(name.keys())[0]