def extendX(x, max_l):
    return str(x * math.ceil(max_l / len(x)))
        

def solution(numbers):  
    numbers.sort(key = lambda x : str(x) * 12, reverse = True)
    
    answer = ''
    for n in numbers:
        answer += str(n)
    
    return str(int(answer))