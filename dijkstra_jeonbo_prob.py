import time
import heapq

start_time=time.time()

INF=int(1e9)
n, m, c=map(int, input().split())
start=c
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

# graph=[[], [(2, 4), (3, 2)]]
for _ in range(m) :
  a, b, c=map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start) :
  q=[]
  heapq.heappush(q, (0, start))
  distance[start]=0

  while q :
    dist, now=heapq.heappop(q)
    if dist < distance[now] :
      continue
    for i in graph[now] :
      cost=dist+i[1]
      if cost < distance[i[0]] :
        distance[i[0]]=cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count=0
max_distance=0

for d in distance :
  if d != INF :
    count += 1  
    max_distance=max(max_distance, d)

print(count-1, max_distance)