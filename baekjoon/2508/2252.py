import sys
# input = sys.stdin.readline
sys.stdin = open("input2508.txt", "r")

N, M = map(int, input().strip().split())
arr = [[[0] for _ in range(N+1)]] * (N+1)
for _ in range(M):
    a, b = map(int, input().strip().split())


print(arr)
