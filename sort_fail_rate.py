def solution(N, stages) :
	all_users = len(stages)
	fails = []
	for i in range(1, N+1) :
		the_user = stages.count(i)
		if the_user == 0 :
			fail_rate = 0
		else :
			fail_rate = the_user / all_users
		fails.append((i, fail_rate))
		all_users -= the_user
	fails.sort(key = lambda x : -float(x[1]))
	result = []
	for fail in fails :
		result.append(fail[0])	
	return result