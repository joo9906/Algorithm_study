import sys
sys.stdin = open("input.txt", "r")

h, w = map(int, input().strip().split())
block = list(map(int, input().strip().split()))
world = [[0]*w for _ in range(h)]
for i in block:


ans = [0] * w
for i in range(1, w-1):
    break
