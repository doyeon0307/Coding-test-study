def calculate(a, b):
    result = set()
    result.add(a + b)
    result.add(a - b)
    result.add(a * b)
    if b != 0:
        result.add(a // b)
    return result

def solution(N, number):
    answer = -1
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        default = int(str(N) * i)
        if default == number:
            return i
        dp[i].add(default)

    for i in range(1, 9):  
        for j in range(1, i):
            for a in dp[i - j]:
                for b in dp[j]:
                    result = calculate(a, b)
                    if number in result:
                        return i
                    dp[i].update(result)
                    
    return answer