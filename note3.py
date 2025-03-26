import sys, heapq
from collections import deque
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline

class Snowman:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr
        self.start_x, self.start_y = -1, -1
        self.target_x, self.target_y = -1, -1
        
        for i in range(n): # 시작, 목표 좌표 찾기
            for j in range(m):
                if arr[i][j] == 2:
                    self.start_x, self.start_y = i, j
                elif arr[i][j] == 3:
                    self.target_x, self.target_y = i, j
                    
        self.weight_map = [[float('inf')] * m for _ in range(n)]
        self.weight_map[self.start_x][self.start_y] = 0
        
        self.delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        self.route()

    def route(self):
        q = [(0, self.start_x, self.start_y)]

        while q:
            base_weight, x, y = heapq.heappop(q)

            for dx, dy in self.delta:
                weight = base_weight
                nx, ny = x + dx, y + dy

                if not(0 <= nx < self.n and 0 <= ny < self.m) or self.weight_map[nx][ny] != float('inf'):
                    continue
                
                if dy != 0 and self.arr[x][y] == 0:
                    continue # 위로 떴는데 좌우로 움직이면 안됨
                
                if dx != 0:
                    weight += 1
                
                if self.weight_map[nx][ny] > weight:
                    self.weight_map[nx][ny] = weight
                    if self.arr[nx][ny] == 1:
                        weight = 0
                    heapq.heappush(q, (weight, nx, ny))

    def result(self):
        return self.weight_map[self.target_x][self.target_y]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solve = Snowman(n, m, arr)
    print(solve.weight_map)
    print(f'#{tc} {solve.result()}')
