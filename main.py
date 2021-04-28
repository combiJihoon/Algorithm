# 00110
# 00011
# 11111
# 00000

# n : 가로, m : 세로
n, m = map(int, input().split())
graph = []
for _ in range(m) :
	graph.append(list(map(int, input().split())))

result = 0

def dfs(x, y) :
	global graph

	if graph[x][y] == 0 :
		graph[x][y] = 1
		dfs(x-1, y)
		dfs(x+1, y)
		dfs(x, y-1)
		dfs(x, y+1)