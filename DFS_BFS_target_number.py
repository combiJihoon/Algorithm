# 인덱스가 다르면 해당 숫자도 다르다.
# 3이 되면 break 하고 다른 수로 넘어간다.
# 큐에는 인덱스를 넣는다.
# 더하거나 뺀 것이 타겟 값이 되면 break

from collections import deque

def solution(numbers, target):
	q = deque()
	
	result = 0
	answer = 0
	for i in range(len(numbers)) :
		q.append((i, -numbers[i]))
		while q :
			index, now = q.popleft()
			result += now
			if result == target :
				answer += 1
				break
			if index + 1 < len(numbers) :
				q.append((index+1, numbers[index+1]))
	return answer

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))
    