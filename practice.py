# visited를 설정해서 방문한 곳은 다시 방문하지 않도록 설정
# 대각선으로만 움직일 수 있으니 델타
# 시간은 상관 없음. 시작점으로 돌아가면 되는 거니까 nx ny가 시작점이면 종료하도록 설정
#


from collections import deque
import sys
sys.stdin = open("input.txt", 'r')

class Dessert:
    def __init__(self, N):
        self.N = N
        self.delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)] # 길이 대각선만 가능하므로 5시, 7시, 11시, 1시
        self.result = 0
        self.visited = [[False] * self.N for _ in range(N)]
        self.start_position = deque([(i, j) for i in range(N) for j in range(N)])

    def middle(self, start):
        while start:
            x, y = start.popleft()


    def tour(self, arr):
        pass



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve = Dessert(N)
    print(solve.start_position)
