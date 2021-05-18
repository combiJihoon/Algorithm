import sys

input = sys.stdin.readline
howManyNum = int(input())
num_list = list(map(int, input().split()))
# +, - , X, // 개수
# n-1개의 조합을 구해서 a면 +, b면 -... 이런식으로 연산
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)
def dfs(i, now) :
	global min_value, max_value, add, sub, mul, div
	if i == howManyNum :
		min_value = min(min_value, now)
		max_value = max(max_value, now)
	else :
		if add > 0 :
			add -= 1
			dfs(i+1, now+num_list[i])
			add += 1
		if sub > 0 :
			sub -= 1
			dfs(i+1, now-num_list[i])
			sub += 1
		if mul > 0 :
			mul -= 1
			dfs(i+1, now*num_list[i])
			mul += 1
		if div > 0 :
			div -= 1
			dfs(i+1, int(now/num_list[i]))
			div += 1

dfs(1, num_list[0])
print(max_value)
print(min_value)
