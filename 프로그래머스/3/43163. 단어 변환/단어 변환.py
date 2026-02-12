from collections import deque

def canSwitch(curr, target):
    diff = 0
    for c in range(len(curr)):
        if (curr[c] != target[c]):
            diff += 1
            if diff > 1:
                return False
    return diff <= 1

def solution(begin, target, words):
    answer = 0
    n = len(words)
    targetIdx = -1
    
    for i in range(n):
        if words[i] == target:
            targetIdx = i
            break

    if targetIdx > -1:
        queue = deque()
        visited = [-1] * n
        
        queue.append(-1)
        
        while queue:
            currIdx = queue.popleft()
            
            if currIdx == targetIdx:
                answer = visited[currIdx]
                break

            curr = words[currIdx] if currIdx > -1 else begin
                        
            # 모든 word 탐색
            for wIdx in range(n):
                if visited[wIdx] > -1:
                    continue

                # 변경 가능한지 확인
                if canSwitch(curr, words[wIdx]):
                    queue.append(wIdx)
                    visited[wIdx] = visited[currIdx] + 1 if currIdx > -1 else 1
    
    return answer