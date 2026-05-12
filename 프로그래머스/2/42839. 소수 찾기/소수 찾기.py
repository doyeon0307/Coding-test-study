from itertools import permutations

def solution(numbers):
    answer = 0
    
    pr = []
    for i in range(1, len(numbers) + 1):
        pr.extend(list(permutations(numbers, i)))
    
    ps = set()
    
    for p in pr:
        ps.add(int(''.join(p)))
    
    for p in ps:
        if p <= 1:
            continue
        sosu = True
        for i in range(2, p):
            if p % i == 0:
                sosu = False
                break
        if sosu:
            answer += 1
            
    return answer