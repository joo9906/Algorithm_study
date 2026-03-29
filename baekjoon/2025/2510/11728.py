import sys, heapq
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

N = int(input())
q = []
answer = 0

for _ in range(N):
    heapq.heappush(q, int(input()))

while len(q) > 1:
    front = heapq.heappop(q)
    back = heapq.heappop(q)
    num = front + back
    answer += num
    heapq.heappush(q,num)

print(answer)