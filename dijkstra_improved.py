import time

start_time=time.time()

import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

# n은 노드 수, m은 간선 정보 수
n, m=map(int, input().split())
start=int(input())

# graph는 노드의 간선 정보
graph=[[] for _ in range(n+1)]

# distance는 최단거리
distance=[INF]*(n+1)

# a : 노드 정보, b : 연결된 노드, c : 거리
for _ in range(m) :
  a, b, c=map(int, input().split())
  graph[a].append(b, c)

def dijkstra(start) :
  q=[]
  # start로 가기 위한 최단거리는 0
  heapq.heappush(q, (0, start))
  distance[start]=0
  # q가 비어있지 않은 동안
  while q : 
    dist, now=heapq.heappop(q)
    if distance[now] < dist :
      continue
    for i in graph[now] :
      cost=dist + i[1]
      if cost < distance[i[0]] :
        distance[i[0]]=cost
        heapq.heappush(cost, i[0])

end_time=time.time()

time_total=end_time-start_time
print(int(time_total))