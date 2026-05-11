import math

def extendX(x, max_l):
    return str(x * math.ceil(max_l / len(x)))[:12]
        

def solution(numbers):
    answer = []
    
    max_l = len(str(numbers[0]))
    for n in numbers:
        answer.append(str(n))
        if len(str(n)) > max_l:
            max_l = len(str(n))
    
    answer.sort(key = lambda x : str(x) * 3, reverse = True)
    
    result = ''
    for a in answer:
        result += a
    
    f = 0
    while result[f] == '0' and f < len(result) - 1:
        f += 1
    
    return result[f:]