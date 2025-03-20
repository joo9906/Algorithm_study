import sys, heapq
from collections import deque
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

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

            if node == self.n-1:
                break

            if distance[node] < weight: # 현재 뽑은 가중치보다 이전에 설정한 가중치가 더 작으면 넘어감
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
for tc in range(1, T+1):
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

