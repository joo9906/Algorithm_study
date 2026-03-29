from itertools import combinations
from collections import deque

n = int(input())

def solve(n):
    ans = []
    tar = list(range(10))

    for i in range(1, 11):
        for j in combinations(tar, i):
                exam = ''.join(map(str, j[::-1]))
                if exam:
                    ans.append(int(exam))
    ans.sort()

    if n < len(ans):
        return ans[n]
    return -1

print(solve(n))