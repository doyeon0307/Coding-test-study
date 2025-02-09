# 출발점 또는 도착점을 감싸고 있으면 받드시 진입/이탈
# 감싸고 있다 = 원 안에 있다
# 원 안에 있다 = 중심과의 거리 < 반지름

def square_of_distance(x1, y1, x2, y2):
  return (x1 - x2) ** 2 + (y1 - y2) ** 2

t = int(input())
answer = []

for _ in range(t):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  
  ans = 0
  for _ in range(n):
    cx, cy, r = map(int, input().split())
    s = r ** 2
    start = square_of_distance(x1, y1, cx, cy) < s
    end = square_of_distance(x2, y2, cx, cy) < s
    if start or end:
      if not(start and end):
        ans += 1
    
  answer.append(ans)

for a in answer:
  print(a)
