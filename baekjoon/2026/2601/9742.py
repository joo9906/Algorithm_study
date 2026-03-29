import sys
from math import factorial
from itertools import permutations

lines = sys.stdin.readlines()

def solve(original_str, k):
    s_list = sorted(list(original_str))
    n = len(s_list)
    target_idx = int(k)

    if target_idx > factorial(n):
        return "No permutation"

    cnt = 0
    for perm in permutations(s_list, n):
        cnt += 1
        if cnt == target_idx:
            return ''.join(perm)

    return "No permutation"

for line in lines:
    parts = line.split()
    if len(parts) != 2:
        continue

    first, second = parts
    print(f'{first} {second} = {solve(first, second)}')