# 내 답
n, m, start = map(int, input().split())

graph = [[-1]*(n+1) for _ in range(n+1)]

for a in range(n+1) :
  for b in range(n+1) :
    if a == b :
      graph[a][b] = 0

for _ in range(m) :
  a, b, c = map(int, input().split())
  graph[a][b] = c

result = -1
count = 0
for i in range(1, n+1) :
  result = max(result, graph[start][i])
  if graph[start][i] > 0 :
    count += 1

print(count, end = ' ')
print(result, end = ' ')

# 해설의 답
