def solution(prices):
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    stack = []
    
    for i, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            l = stack.pop()
            answer[l[0]] = i - l[0]
        stack.append([i, p])
                
    return answer