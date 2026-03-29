import sys, heapq
input = sys.stdin.readline
# sys.stdin = open("input2508.txt", "r")

n = int(input().strip())
m = int(input().strip())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().strip().split())
    adj[a].append((w, b))

start, end = map(int, input().strip().split())

INF = 10**18
dist = [INF] * (n + 1)
dist[start] = 0

pq = [(0, start)]
while pq:
    cost, u = heapq.heappop(pq)
    if cost != dist[u]:
        continue
    if u == end:
        print(cost)
        break
    for w, v in adj[u]:
        nc = cost + w
        if nc < dist[v]:
            dist[v] = nc
            heapq.heappush(pq, (nc, v))