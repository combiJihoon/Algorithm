n = int(input())
grades = []
for _ in range(12) :
	grades.append(tuple(input().split()))

# 국어점수 기준 1차 정렬
grades.sort(key = lambda x : ((-(x[1])), x[2], (-(x[3])), x[0]))

for name in grades :
	print(name[0])


