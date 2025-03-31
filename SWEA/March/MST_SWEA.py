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

# 다익스트라- 상원이의 기차여행 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

import heapq

class Train:
    def __init__(self, n, arr):
        self.n = n
        self.graph = arr
        self.lis = self.dijkstra(0)
        self.result = self.lis[-1]

    def dijkstra(self, start_node):
        q = [(0, start_node)]
        distance = [float('inf')] * self.n
        distance[start_node] = 0

        while q:
            weight, node = heapq.heappop(q)

            if node == self.n - 1:
                break

            if distance[node] < weight:  # 현재 뽑은 가중치보다 이전에 설정한 가중치가 더 작으면 넘어감
                continue

            for info in graph[node]:
                next_node = info[0]
                next_dist = info[1]

                ndist = weight + next_dist

                if distance[next_node] > ndist:
                    distance[next_node] = ndist
                    heapq.heappush(q, (ndist, next_node))

        return distance


T = int(input())
for tc in range(1, T + 1):
    n, t = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(t):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))

    solve = Train(n, graph)

    if solve.result < float('inf'):
        print(f'#{tc} {solve.result}')
    else:
        print(f'#{tc} impossible')

# 누군가의 속마음 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
import heapq

class Marry:
    def __init__(self, Y, X, N, village):
        self.momy = Y
        self.momx = X
        self.N = N
        self.village = village
        self.delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def route(self):
        q = [(self.village[self.momy][self.momx], self.momy, self.momx)]
        weight_village = [[float('inf')] * self.N for _ in range(N)]
        weight_village[self.momy][self.momx] = village[self.momy][self.momx]

        while q:
            weight, x, y = heapq.heappop(q)

            if weight_village[x][y] < weight:
                continue

            for dx, dy in self.delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.N and 0 <= ny < self.N and self.village[nx][ny] >= 0:
                    new_w = weight + self.village[nx][ny]
                    if weight_village[nx][ny] > new_w:
                        weight_village[nx][ny] = new_w
                        heapq.heappush(q, (new_w, nx, ny))

        mv = 0
        for i in range(self.N):
            for j in range(self.N):
                if weight_village[i][j] == float('inf'):
                    continue

                if mv < weight_village[i][j]:
                    mv = weight_village[i][j]

        return mv

T = int(input())
for tc in range(1, T + 1):
    Y, X = map(int, input().split())
    N = int(input())
    village = [list(map(int, input().split())) for _ in range(N)]
    solve = Marry(Y, X, N, village)
    print(f'#{tc} {solve.route()}')

# 최소 스패닝 트리

# prim 버전
class Prim:
    def __init__(self, V, E, data, adj):
        self.V = V
        self.E = E
        self.data = data
        self.adj = adj

    def solve(self, start_node):
        MST = [False] * (self.V+1) # 방문을 했다고 넣을 것
        q = [(0, start_node)] # 맨 처음 뽑을 대상의 가중치는 0, 시작 노드
        min_weight = 0

        while q:
            weight, node = heapq.heappop(q)

            if MST[node]: # 뽑아다가 쓴 적 있는 간선이라면 지나감
                continue

            MST[node] = True
            min_weight += weight # 간선의 최소 가중치에 더함 - 여기에서 더하는 이유는 최소 가중치 간선을 뽑아온거기 때문

            for i in range(node, self.V + 1):
                if self.adj[node][i] == float('inf'):
                    continue

                if MST[i]:
                    continue

                # 인접 행렬에서 의미가 있는 자료인 경우에만 아래를 실행
                new_w = self.adj[node][i]
                heapq.heappush(q, (new_w, i))

        return min_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(E)]
    adj = [[] for _ in range(V + 1)]
    for node, target, w in data:
        adj[node][target] = w
        adj[target][node] = w

    ans = Prim(V, E, data, adj)
    print(f'#{tc} {ans.solve(1)}')

# 크루스칼 버전
def find(x):
    global parents

    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    global parents

    rx = find(x)
    ry = find(y)

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(E)]
    data.sort(key=lambda x: x[2])
    parents = [i for i in range(V + 1)]  # 노드가 1번부터 시작하니까 0번째는 버릴거임

    cnt = 0
    min_weight = 0

    for k in data:
        start, target, weight = k
        if find(start) != find(target):  # 둘이 연결이 되어있지 않은 상태일 때 실행
            union(start, target)
            cnt += 1
            min_weight += weight

        if cnt == V - 1:
            break

    print(f'#{tc} {min_weight}')