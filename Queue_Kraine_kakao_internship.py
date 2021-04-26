def solution(board, moves):
	answer = 0
	temp = [0]
	for move in moves :
		# 열 별로 확인
		dx = move - 1
		for i in range(len(board)) :
			if board[i][dx] != 0 :
				temp.append(board[i][dx])
				answer += check(temp) # temp의 원소와 같은지 확인
				board[i][dx] = 0
				break

	return answer

# 같은 값인지 확인하는 함수
def check(my_list) :
	count = 0
	# if len(my_list) >= 2 :
	if my_list[len(my_list)-1] == my_list[len(my_list)-2] :
		my_list.pop(len(my_list)-1)
		my_list.pop(len(my_list)-1)
		count += 2

	return count
​