# 인덱스가 다르면 해당 숫자도 다르다.
# 3이 되면 break 하고 다른 수로 넘어간다.
# 큐에는 인덱스를 넣는다.
# 더하거나 뺀 것이 타겟 값이 되면 break

from collections import deque

def solution(numbers, target):
    q = deque()
    q.append((0, 0))
    answer = 0

    while q :
        curr_sum, index = q.popleft()
        if index == len(numbers) :
            if curr_sum == target :
                answer += 1
        else :
            new_num = numbers[index]
            q.append((curr_sum + new_num, index+1))
            q.append((curr_sum - new_num, index+1))
    return answer

