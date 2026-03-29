import sys, heapq
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

N = int(input().strip())
q = []
for _ in range(N):
    heapq.heappush(q, int(input().strip()))
    half = len(q) // 2
    if len(q) % 2 == 0:
        print(heapq.nsmallest(half, q)[-1])
    else:
        print(heapq.nsmallest(half+1, q)[-1])
