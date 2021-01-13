# 내 답
# n, m, start = map(int, input().split())

# graph = [[-1]*(n+1) for _ in range(n+1)]

# for a in range(n+1) :
#   for b in range(n+1) :
#     if a == b :
#       graph[a][b] = 0

# for _ in range(m) :
#   a, b, c = map(int, input().split())
#   graph[a][b] = c

# result = -1
# count = 0
# for i in range(1, n+1) :
#   result = max(result, graph[start][i])
#   if graph[start][i] > 0 :
#     count += 1

# print(count, end = ' ')
# print(result, end = ' ')



# 해설의 답
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start) :
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q :
    dist, now = heapq.heappop(q)
    for i in graph[now] :
      if distance[now] < dist :
        continue
      cost = dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  
dijkstra(start)

count = 0
max_distance = 0

for d in distance :
  # 도달할 수 있는 경우에는 INF가 아니다.
  if d != INF :
    count += 1
    max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1
print(count-1, max_distance)
