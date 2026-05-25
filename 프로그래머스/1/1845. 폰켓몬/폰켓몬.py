def solution(nums):
    answer = 0
    
    p = {}
    
    for n in nums:
        p[n] = p.get(n, 0) + 1    
    
    return min(len(p.keys()), len(nums) // 2)