import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline



n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
