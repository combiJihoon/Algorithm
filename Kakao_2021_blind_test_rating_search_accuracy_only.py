info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# new_info = []
# for i in info :
# 	new_info.append(i.split(" "))
# print(new_info)

# new_query = []
# for q in query :
# 	new_temp = q.split(" ")
# 	for i in new_temp :
# 		if i == 'and' :
# 			new_temp.remove(i)
# 	new_query.append(new_temp)
# print(new_query)

# Big(O) = n^2 + n

def solution(info, query) :
	new_info = []
	for i in info :
		new_info.append(i.split(" "))

	new_query = []
	for q in query :
		new_temp = q.split(" ")
		for i in new_temp :
			if i == 'and' :
				new_temp.remove(i)
		new_query.append(new_temp)

	result = []
	for query in new_query :
		temp = 0
		for info in new_info :
			i = 0
			while i < 5 :
				if query[i] == info[i] or query[i] == '-' :
					i += 1
					if i == 4 and int(info[4]) >= int(query[4]) :
						temp += 1
						break
				else :
					break
		result.append(temp)

	return result

print(solution(info, query))


		