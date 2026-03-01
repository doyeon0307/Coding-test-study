def solution(m, n, puddles):
    answer = 0
    
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1
    
    min_1_x = m + 1
    min_y_1 = n + 1
    
    for p in puddles:
        x, y = map(int, p)
        if y == 1:
            min_1_x = min(min_1_x, x)
        if x == 1:
            min_y_1 = min(min_y_1, y)
    
    for y in range(1, n + 1):
        if y < min_y_1:
            dp[y][1] = 1

    for x in range(1, m + 1):
        if x < min_1_x:
            dp[1][x] = 1


    for y in range(2, n + 1):
        for x in range(2, m + 1):
            if [x, y] in puddles:
                continue                
                
            up = dp[y - 1][x]
            left = dp[y][x - 1]
            
            dp[y][x] = up + left
    
    return dp[n][m] % 1_000_000_007