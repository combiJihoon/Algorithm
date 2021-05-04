# 1이 아니면 이동하지 않는다.
# 1이면 이동한다.
# 상하좌우 살피고 이동하면 +1

# n : 세로, m : 가로
n, m = map(int, input().split())
graph = []
for _ in range(n) :
	graph.append(list(map(int, input())))

# 하, 좌, 우 -> '상'으로는 이동하지 않음
dx = [0, -1, 1]
dy = [1, 0, 0]

x = y = 0
def dfs(x, y) :
	for i in range(3) :
		nx = x + dx[i]
		ny = y + dy[i]
		# graph 내부이며 값이 1이면 이동
		if nx >= 0 and nx <= m-1 and ny >= 0 and ny <= n-1 :
			if graph[ny][nx] == 1 :
				graph[ny][nx] = graph[y][x] + 1
				# 이동
				x = nx
				y = ny
				dfs(x, y)
			if x == m-1 and y == n-1 :
				break
		
dfs(0, 0)
print(graph[n-1][m-1])



# 101010
# 111111
# 000001
# 111111
# 111111