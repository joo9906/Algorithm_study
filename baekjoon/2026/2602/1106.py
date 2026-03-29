import sys
input = sys.stdin.readline
# sys.stdin = open("../input.txt", "r")

C, N = map(int, input().strip().split())
inform = [list(map(int, input().strip().split())) for _ in range(N) ]

dp = [10e9] * (C + 1001)
dp[0] = 0

for cost, people in inform:
    for i in range(people, C + 1001):
        if dp[i - people] != 10e9:
            dp[i] = min(dp[i], dp[i-people] + cost)

print(min(dp[C:]))