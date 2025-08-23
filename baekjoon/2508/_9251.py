import sys
from itertools import combinations
import time
#input = sys.stdin.readline
sys.stdin = open('input2508.txt.', 'r')

first = input().strip()
second = input().strip()
ans = 0

for i in range(len(first)-1, 0, -1):
    for a in combinations(first, i):
        for b in combinations(second, i):
            if a == b:
                ans = max(ans, len(a))

print(ans)
