info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import combinations as comb
from collections import defaultdict

def solution(info, query) :
	info_dict = defaultdict(list)
	answer = []
	for i in info :
		i = i.split()
		info_key = i[:-1]
		info_value = int(i[-1])
		# 4가지 정보를 조합으로 만든다.
		for i in range(5) :
			for c in comb(info_key, i) :
				temp_key = "".join(c)
				info_dict[temp_key].append(info_value)
	for key in info_dict.keys() :
		info_dict[key].sort()
	# query에서 and와 - 제거 하고 value값 가져오기
	for q in query :
		q = q.split()
		for i in range(3) :
			q.remove('and')
		while '-' in q :
			q.remove('-')
		qeury_value = q[:-1]
		query_score = int(q[-1])
		temp_q = "".join(qeury_value)

		if temp_q in info_dict :
			score_list = info_dict[temp_q]
			if len(score_list) > 0 : 
				# start와 end가 같아도 됨
				start, end = 0, len(score_list)
				while start < end :
					mid = (start + end) // 2
					if score_list[mid] >= query_score :
						end = mid
					else :
						start = mid+1
				answer.append(len(score_list)-start)
			else :
				answer.append(0)

	return answer

print(solution(info, query))

# [1, 2, 3, 4, 5]
#  s	t  m       e
#  s m=t e
# s=m e
#    s=e           => break



