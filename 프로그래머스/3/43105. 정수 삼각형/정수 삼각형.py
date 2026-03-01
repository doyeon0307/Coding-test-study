def solution(triangle):
    answer = 0
    
    height = len(triangle)
    dp = [[0 for _ in range(height)] for _ in range(height)]
    
    dp[0][0] = triangle[0][0]
    
    for h in range(1, height):
        for i, t in enumerate(triangle[h]):
            sum = t + dp[h - 1][i - 1] if i - 1 >= 0 else 0
            dp[h][i] = max(dp[h][i], t + dp[h-1][i], sum)
            
    return max(dp[-1])