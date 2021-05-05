# 인구 수가 주어졌을 때 인구 이동 몇 번 발생하는 지 
# r행 c열
from collections import deque

# n by n 크기의 땅, l <= 인구 수 <= r
n, l, r = map(int, input().split())
graph = []
visited = []
toBeCombinated = []
for _ in range(n) :
	graph.append(list(map(int, input().split())))
	# 방문 여부 확인
	visited.append([0 for i in range(n)])
	# 연합할 국가들 리스트
	toBeCombinated.append([0 for i in range(n)])

answer = 0
# 인접한 나라의 위치 인덱스 리턴
# 현재 위치 인덱스 : x, y
# 상하좌우 돌며 확인
def nearestChecker(x, y) :
	global visited
	global toBeCombinated
	global answer

	q = deque()
	q.append((x, y))
	visited[x][y] = 1

	dx = [0, 0, -1, 1] # 행
	dy = [-1, 1, 0, 0] # 열

	while q :
		x, y = q.popleft()
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1 :
				if visited[nx][ny] == 0 :
					# 방문
					i, j = nx, ny
					# 방문한 곳은 1로 만들기
					visited[i][j] = 1
					# True면 연합할 나라의 인구 수 추가하기
					if numDiffChecker(x, y, i, j) :
						if toBeCombinated[x][y] == 0 :
							toBeCombinated[x][y] = graph[x][y]
						if toBeCombinated[i][j] == 0 :
							toBeCombinated[i][j] = graph[i][j]
					q.append((i, j))

	changedNum = numOfPeople()
	if not changedNum :
		return 
	else :
		answer += 1
		clearChange(changedNum)		
		nearestChecker(x, y)	

# 인구 수 차이가 l과 r 사이인지 체크
# x, y 는 위치 인덱스
def numDiffChecker(x, y, i, j) :
	global graph
	temp = graph[x][y] - graph[i][j]
	if temp < 0 :
		numDiff = -temp
	else :
		numDiff = temp
	if numDiff >= l and numDiff <= r :
		return True
	else :
		return False

# 연합한 나라들의 총 인구 수
def numOfPeople() :
	global toBeCombinated
	# 연합 나라 수 
	count = 0
	totalNum = 0
	for i in range(n) :
		for j in range(n) :
			if toBeCombinated[i][j] != 0 :
				count += 1
				totalNum != toBeCombinated[i][j]
	if count == 0 :
		return False
	else :
		changedNum = totalNum / count
		return changedNum

# graph 다시 채우기
def clearChange(changedNum) :
	global graph
	global toBeCombinated

	for i in range(n) :
		for j in range(n) :
			if toBeCombinated[i][j] != 0 :
				graph[i][j] = changedNum
				# 연합에 참여했던 국가들 다시 제거
				toBeCombinated[i][j] = 0 

nearestChecker(0, 0)
print(answer)
