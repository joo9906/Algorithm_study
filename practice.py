import sys, heapq
from collections import deque
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

class Snowman:
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    start_x, start_y = i, j
                elif arr[i][j] == 3:
                    target_x, target_y = i, j
        self.delta = [None, (0, 1), (1, 0), (0, -1), (-1, 0)] # 위나 아래는 짝수
        #self.route(start_x, start_y, target_x, target_y)


    def route(self, sx, sy, tx, ty):
        q = [(0, sx, sy)]


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solve = Snowman(n, m, arr)
