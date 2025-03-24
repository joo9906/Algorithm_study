# 하나로
import sys, heapq
from collections import deque
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

# 최적화 안된 prim
def prim(tax):
    q = [(0, 0)] # 비용, 노드
    visited = [0] * N
    min_cost = 0
    dists = [float('inf')] * N
    dists[0] = 0

    while q:
        cost, node = heapq.heappop(q)

        if visited[node] == 1:
            continue

        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node] == 1:
                continue

            new_cost = ((island_x[next_node] - island_x[node]) ** 2 + (island_y[next_node] - island_y[node]) ** 2) * tax
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return round(min_cost)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    tax = float(input())
    result = prim(tax)
    print(f'#{tc} {result}')

# 최적화 된 prim
def prim(tax):
    q = [(0, 0)]  # 비용, 노드
    visited = [0] * N
    min_cost = 0

    while q:
        cost, node = heapq.heappop(q)

        if visited[node] == 1:
            continue

        visited[node] = 1
        min_cost += cost

        for next_node in range(N):
            if visited[next_node] == 1:
                continue

            new_cost = ((island_x[next_node] - island_x[node]) ** 2 + (island_y[next_node] - island_y[node]) ** 2) * tax
            heapq.heappush(q, (new_cost, next_node))

    return round(min_cost)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    tax = float(input())
    result = prim(tax)
    print(f'#{tc} {result}')

# Kruskal 알고리즘으로 푼거 - 얘는 다익스트라로 안풀림

def find(x):
    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return

    if rootx < rooty:
        parents[rooty] = rootx
    else:
        parents[rootx] = rooty

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    tax = float(input())
    mincost = 0
    parents = [i for i in range(N)]

    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            cost = ((island_x[i] - island_x[j]) ** 2 + (island_y[i] - island_y[j]) ** 2) * tax
            edges.append((i, j, cost))

    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mincost += w

    print(f'#{tc} {round(mincost)}')

