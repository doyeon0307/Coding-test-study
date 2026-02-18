def solution(n, costs):
    answer = 0

    costs.sort(key = lambda x : x[2])
    islands = [False for _ in range(n)]
    
    islands[costs[0][0]] = True
    islands[costs[0][1]] = True
    answer += costs[0][2]
    costs[0][2] = -1

    while False in islands:
        for i, c in enumerate(costs):
            x, y, w = map(int, c)
            if w >= 0 and (islands[x] or islands[y]):
                if islands[x] and islands[y]:
                    continue
                islands[x] = True
                islands[y] = True
                answer += w
                costs[i][2] = -1
                break
        
    return answer