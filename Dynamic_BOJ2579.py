# 연속 두번 올라갔으면 0으로 만든다.
# 하나 뛰어서 오르는 것은 당연히 가능
# n = 6
# stairs = [10, 20, 15, 25, 10, 20]

import sys

input = sys.stdin.readline
n = int(input())

stairs = [0 for i in range(300)]
dp = [0 for i in range(300)]
for i in range(n):
    stairs[i] += int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

print(dp[n-1])
