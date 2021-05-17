# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.



from collections import deque
from itertools import permutations as pm
import sys

input = sys.stdin.readline
howManyNum = int(input())
num_list = list(map(int, input().split()))
# +, - , X, // 개수
# n-1개의 조합을 구해서 a면 +, b면 -... 이런식으로 연산
add, sub, mul, div = map(int, input().split())

# howManyCal 인덱스의 조합 구하기
temp_cal = []
temp_cal += ["add"]*add
temp_cal += ["sub"]*sub
temp_cal += ["mul"]*mul
temp_cal += ["div"]*div

pmd_cal = []
pmd_cal += pm(temp_cal, len(temp_cal))
pmd_cal = list(set(pmd_cal)) # 중복제거

maxResult = -int(1e9)
minResult = int(1e9)
for pmd in pmd_cal :
	q = deque(pmd)
	while q :
		std = num_list[0]
		for i in range(1, len(num_list)) :
			t = q.popleft()
			if t == 'add' : 
				std += num_list[i]
			elif t == 'sub' : 
				std -= num_list[i]
			elif t == 'mul' : 
				std *= num_list[i]
			elif t == 'div' : 
				if std < 0 :
					std = -int((-std)/num_list[i])

				else :
					std //= num_list[i]
		maxResult = max(maxResult, std)
		minResult = min(minResult, std)

print(maxResult)
print(minResult)






