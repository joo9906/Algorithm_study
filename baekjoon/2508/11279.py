import sys, heapq
input = sys.stdin.readline
# sys.stdin = open("input2508.txt", "r")

n = int(input().strip())
arr = []
heapq.heapify(arr)
for _ in range(n):
    x = int(input().strip())
    if x == 0:
        if arr:
            print(-(heapq.heappop(arr)))
        else:
            print(0)
    else:
        heapq.heappush(arr, -x)