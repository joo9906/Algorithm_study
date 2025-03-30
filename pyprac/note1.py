import heapq
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
input = sys.stdin.readline

class Prim:
    def __init__(self, n, m):
        self.n = n # 노드의 개수
        self.m = m # 간선의 개수

    def solve(self, graph):
        MST = [False] * (self.n+1)
        q = [(0, 1)]
        min_weight = 0

        while q:
            weight, node = heapq.heappop(q)

            if MST[node]:
                continue

            min_weight += weight
            MST[node] = True

            for i in graph[node]:
                nw, nn = i
                if MST[nn]:
                    continue

                heapq.heappush(q, (nw, nn))

        return min_weight


n = int(input().strip())
m = int(input().strip())
data = [tuple(map(int, input().strip().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]

for start, end, weight in data: # 양방향 그래프로 만들어 줌
    graph[start].append((weight, end))
    graph[end].append((weight, start))

ans = Prim(n, m)
print(ans.solve(graph))


