# 장훈이의 높은 선반
from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')

class shelve:
    def __init__(self, n, b, height):
        self.n = n # 난쟁이의 머릿수
        self.target = b # 목표로 하는 높이(이거 이상으로는 갈 수 있음)
        self.height = height # 난쟁이들의 키가 적힌 리스트
        self.min_diff = float('inf') # 목표값과 난쟁이들 탑 사이의 높이 차이
        self.solve()

    def solve(self):
        for k in range(1, n + 1): # 쌓는 난쟁이 머릿수 k
            for com in combinations(self.height, k):
                top = sum(com)

                if top >= self.target:
                    diff = top-self.target

                    if diff < self.min_diff:
                        self.min_diff = diff

T = int(input())

for tc in range(1, T + 1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))

    shel = shelve(n, b, height)
    print(f'#{tc} {shel.min_diff}')

# N-Queen
class Queen:
    def __init__(self, N):
        self.n = N
        board = [[0] * N for _ in range(N)]
        self.max_queen = 0
        # 퀸이 갈 수 있는 방향
        self.delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        self.result = self.put(board, 0)

    def check(self, board, x, y):
        for dx, dy in self.delta: # 델타를 돌면서 본인을 공격 가능한 퀸이 있는지 확인
            nx = x + dx
            ny = y + dy
            while 0 <= nx < self.n and 0 <= ny < self.n:
                if board[nx][ny] == 1:
                    return False
                nx += dx
                ny += dy

        return True

    def put(self, board, row):
        if row == self.n:
            return 1

        cnt = 0
        for col in range(self.n):
            if self.check(board, col, row):
                board[col][row] = 1
                cnt += self.put(board, row + 1)
                board[col][row] = 0

        return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    solve = Queen(N)
    print(f'#{tc} {solve.result}')

# 최대 상금
class Win:
    def __init__(self, num, change):
        self.num = num  # 주어지는 숫자 배열 리스트
        self.change = change  # 바꿔야 하는 횟수
        self.visited = set()
        self.max_result = ['0']
        self.exchange(num, change)

    def exchange(self, num, change, cnt=0):
        if cnt == change:  # cnt번 만큼 돌렸으면 끝, 최대값을 현재 값으로 바꿀 수 있나 확인하고 가능하면 바꿈
            self.max_result[0] = max(self.max_result[0], ''.join(num))
            return

        target = ''.join(num)
        if target in self.visited:  # 만든 적 있는 배열이면 중단
            return

        self.visited.add(target)

        N = len(target)
        for i in range(N):
            for j in range(i + 1, N):
                num[i], num[j] = num[j], num[i]
                self.exchange(num, change, cnt + 1)
                num[i], num[j] = num[j], num[i]  # 원상복구


T = int(input())
for tc in range(1, T + 1):
    num, change = map(int, input().split())
    num = list(str(num))  # 문자열 리스트로 찢어서 넣음

    prize = Win(num, change)
    print(f'#{tc} {prize.max_result[0]}')

# 보급로
class Recover:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def route(self, arr):
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[1e9] * self.n for _ in range(self.n)]
        visited[0][0] = arr[0][0]
        q = [(arr[0][0], 0, 0)]

        while q:
            wv, x, y = heapq.heappop(q)

            if wv > visited[x][y]: # 더 짧은 경로로 방문 시 넘어감
                continue

            if x == self.n-1 and y == self.n-1:
                return wv

            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n:
                    nwv = wv + arr[nx][ny]
                    if nwv < visited[nx][ny]:
                        visited[nx][ny] = nwv
                        heapq.heappush(q, (nwv, nx, ny))

    def result(self):
        return self.route(self.arr)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    solve = Recover(n, arr)
    print(f'#{tc} {solve.result()}')


