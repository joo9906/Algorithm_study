import sys
input = sys.stdin.readline
# sys.stdin = open("input2508.txt", "r")

N, M = map(int, input().strip().split())
arr = [0] + list(map(int, input().strip().split()))

for _ in range(M):
    left, right = map(int, input().strip().split())
    cur = 0
    while left <= right:
        cur += arr[left]
        left += 1

    print(cur)