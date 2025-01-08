from collections import deque

n, k = map(int, input().split())

limit = 100000

visted = [-1 for _ in range(limit + 1)]
time, count = 0, 0

a = deque()
a.append(n)
visted[n] = 0

while a:
  x = a.popleft()

  if x == k:
    time = visted[x]
    count += 1
    continue

  for i in [x - 1, x + 1, 2 * x]:
    if i >= 0 and i <= limit and (visted[i] == -1 or visted[i] == visted[x] + 1):
      a.append(i)
      visted[i] = visted[x] + 1


print(time)
print(count)