import sys
import heapq
#input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

n = int(input().strip())
q = []
heapq.heapify(q)

for _ in range(n):
    target = int(input().strip())
    if target == 0:
        if not q:
            print(0)
        else:
            now = heapq.heappop(q)
            print(now)

    else:
        heapq.heappush(q,target)