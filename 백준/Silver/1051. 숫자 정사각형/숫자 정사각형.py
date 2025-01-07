n, m = map(int, input().split())

a = []

for _ in range(n):
  row = input()
  a.append([int(x) for x in row])

result = 1

for i in range(n):
  for j in range(m - 1):
    for k in range(j + 1, m):
      if a[i][j] == a[i][k]:
        r = a[i][j]
        l = k - j
        if i + l >= n:
          break
        else:
          if a[i + l][j] == r and a[i + l][k] == r:
            l += 1
            if result < l * l:
              result = l * l

print(result)