import sys
from collections import defaultdict
input = sys.stdin.readline
# sys.stdin = open("input.txt", 'r')

N = int(input())
files = []
ans = defaultdict(int)

for _ in range(N):
    name, ext = map(str, input().strip().split('.'))
    ans[ext] += 1

last = []
for a, b in ans.items():
    last.append((a, b))
last.sort()

for ex, cnt in last:
    print(ex, cnt)