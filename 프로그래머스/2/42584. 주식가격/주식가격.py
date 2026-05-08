def solution(prices):
    answer = [len(prices) - i - 1 for i in range(len(prices))]
    stack = []
    
    for i, p in enumerate(prices):
        while stack and p < stack[-1][1]:
            idx = stack.pop()[0]
            answer[idx] = i - idx
        stack.append([i, p])
    
    return answer