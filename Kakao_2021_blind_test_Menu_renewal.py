# ordered at leat two times
# 알파벳 조합 리스트 만들어서 개수 추가해야 할듯

from itertools import combinations, permutations
# from collections import Counter

def solution(orders, course) :
	answer = []

	for c in course :
		temp = []
		menu_candidate = {}
		for order in orders :
			temp += combinations(sorted(order), c)
			
		for t in temp :
			key = "".join(t)
			if key in menu_candidate :
				menu_candidate[key] += 1
			else :
				menu_candidate[key] = 1
		

		for menu in menu_candidate :
			if max(menu_candidate.values()) > 1 :
				if menu_candidate[menu] == max(menu_candidate.values()) :
					answer.append(menu)

	return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))


# def solution(orders, course) :
# 	answer = []

# 	for c in course :
# 		temp = []
# 		menu_dict = {}
# 		for o in orders :
# 			temp += combinations(sorted(o), c)
# 		most_ordered = Counter(temp).most_common()
# 		answer += [a for a, v in most_ordered if v > 1 and v == most_ordered[0][1]]
# 	return ["".join(i) for i in sorted(answer)]


