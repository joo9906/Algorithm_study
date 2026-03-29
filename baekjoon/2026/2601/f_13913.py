import heapq
import sys

input = sys.stdin.readline
# sys.stdin = open("input.txt", 'r')

n, k = map(int, input().strip().split())

MAX_SIZE = 100000

q = [(0, n, [n])]
heapq.heapify(q)
check = {n}

while q:
    time, location, path = heapq.heappop(q)

    if location == k:
        print(time)
        print(*path)
        break

    for next_loc in (location - 1, location + 1, location * 2):
        if 0 <= next_loc <= MAX_SIZE and next_loc not in check:
            check.add(next_loc)
            heapq.heappush(q, (time + 1, next_loc, path+[next_loc]))