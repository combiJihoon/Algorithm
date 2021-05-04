# 00110
# 00011
# 11111
# 00000

# n : 가로, m : 세로
n, m = map(int, input().split())
graph = []
for _ in range(m) :
	graph.append(list(map(int, input())))

result = 0

def dfs(x, y) :
	if x < 0 or x >= n or y < 0 or y >= m :
		return False

	if graph[x][y] == 0 :
		graph[x][y] = 1
		dfs(x-1, y) 
		dfs(x, y+1)
		dfs(x+1, y)
		dfs(x, y-1)

		return True
	return False

for i in range(n) :
	for j in range(m) :
		if dfs(i, j) == True :
			result += 1

print(result)