import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def solve(arr):
    plat = [[] for _ in range(7)]
    cnt = 0

    for line_num, plat_num in arr:
        while plat[line_num] and plat[line_num][-1] > plat_num:
            plat[line_num].pop()
            cnt += 1

        if plat[line_num] and plat[line_num][-1] == plat_num:
            continue

        plat[line_num].append(plat_num)
        cnt += 1

    return cnt

n, p = map(int, input().split())
arr = [tuple(map(int, input().strip().split())) for _ in range(n)]
print(solve(arr))