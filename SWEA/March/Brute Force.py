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

# N-Queen ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

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

# 최대 상금 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

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

# 보급로 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

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

# 미생물 군집 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

class Virus:
    def __init__(self, N, M, K, state):
        self.N = N # 전체 판의 크기(N*N)
        self.M = M # 격리 시간
        self.K = K # 미생물 군집의 수(input에서 9줄)
        self.remain_virus = 0
        self.dx = [None, -1, 1, 0, 0] # 1~4로 받으니까 빈거 하나 앞에 줌
        self.dy = [None, 0, 0, -1, 1]

    def change_direction(self, direction):
        # 주어진 인풋에서 상 = 1, 하 = 2 / 좌 = 3, 우 = 4 이므로 해당 순서대로. 바꿔줌
        if direction == 1:
            return 2
        elif direction == 2:
            return 1
        elif direction == 3:
            return 4
        elif direction == 4:
            return 3

    def check(self, state):
        dict = {}
        result = deque([])

        for _ in range(len(state)): # 같은 좌표인 애들의 값을 합치는 부분
            x, y, head, direction = state.popleft()
            key = (x, y)

            # 3, 4개 군집이 모였을 때 세개를 다 비교해야 하는데 하나씩만 비교했음. dict value 안에 머릿수, 방향, 최대 머릿수를 넣음
            if key in dict:
                dict[key][0] += head
                if dict[key][2] < head:
                    dict[key][1] = direction
                    dict[key][2] = head
            else:
                dict[key] = [head, direction, head]

        for k in dict:
            x, y = k
            h = dict[k][0]
            d = dict[k][1]
            result.append((x, y, h, d))

        return result

    def after_time(self, state, time):
        if time == self.M:
            for b in state:
                x, y, h, d = b
                self.remain_virus += h
            return

        for _ in range(len(state)): # 미생물들이 1시간 뒤 본인의 방향으로 전진하고 일어나는 일을 하는 함수
            x, y, head, direct = state.popleft()

            nx = x + self.dx[direct]
            ny = y + self.dy[direct]

            if nx == 0 or ny == 0 or nx == self.N-1 or ny == self.N - 1:
                head //= 2
                direct = self.change_direction(direct)

            ap = [nx, ny, head, direct]
            state.append(ap)
        self.after_time(self.check(state), time + 1)

    def end(self):
        return self.remain_virus

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    state = deque([list(map(int, input().split())) for _ in range(K)])
    solve = Virus(N, M, K, state)
    solve.after_time(state, 0)
    print(f'#{tc} {solve.end()}')
# 디저트 카페ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# visited를 설정해서 방문한 곳은 다시 방문하지 않도록 설정
# 대각선으로만 움직일 수 있으니 델타
# 시간은 상관 없음. 시작점으로 돌아가면 되는 거니까 nx ny가 시작점이면 종료하도록 설정
# 조건 1. 대각선으로 이동
# 조건 2. 같은 숫자를 방문하면 안됨(시작점 제외)
# 조건 3. 왔던 길 다시 돌아가면 안됨
# 조건 4. 하나의 카페에서 디저트 먹으면 안된다(길이 1 안됨)

import sys
sys.stdin = open("input.txt", 'r')

class Dessert:
    def __init__(self, N, arr):
        self.N = N
        self.arr = arr
        self.delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        self.result = -1 # 도착이 불가능하면 -1이 출력되어야 함
        for i in range(N):
            for j in range(N):
                self.dfx(i, j, i, j, 0, {arr[i][j]})


    def dfx(self, sx, sy, x, y, direction, save):
        for i in range(direction, 4):
            nx = x + self.delta[i][0]
            ny = y + self.delta[i][1]

            if nx == sx and ny == sy: # 출발점으로 돌아올 수 있으면 result랑 비교해서 더 큰 값을 결과로 저장
                if len(save) > 2:
                    self.result = max(self.result, len(save))
                return

            # 범위를 벗어나지 않고
            if 0 <= nx < self.N and 0 <= ny < self.N and self.arr[nx][ny] not in save: # 갔던 곳도 아니라면
                save.add(arr[nx][ny])
                self.dfx(sx, sy, nx, ny, i, save) # 갔던 방향은 제외할거니까 방향에 i를  넣어줌
                save.remove(arr[nx][ny]) # 갔던 방향을 범위에서 제거, 다른 방향으로 갈 수 있게 됨

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve = Dessert(N, arr)
    print(f'#{tc} {solve.result}')

# 디저트 카페 클래스 안 쓴 버전 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def dessert(N, arr):
    delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # 대각선 이동
    result = -1  # 결과 저장

    def dfs(sx, sy, x, y, direction, save):
        nonlocal result
        for i in range(direction, 4):
            nx, ny = x + delta[i][0], y + delta[i][1]

            if nx == sx and ny == sy:  # 출발점으로 돌아올 수 있으면 result랑 비교해서 더 큰 값을 결과로 저장
                if len(save) > 2:
                    result = max(result, len(save))
                return

            # 범위를 벗어나지 않고
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] not in save:  # 갔던 곳도 아니라면
                save.add(arr[nx][ny])
                dfs(sx, sy, nx, ny, i, save)  # 갔던 방향은 제외할거니까 방향에 i를  넣어줌
                save.remove(arr[nx][ny])  # 갔던 방향을 범위에서 제거, 다른 방향으로 갈 수 있게 됨

    # 모든 칸을 시작점으로 해서 DFS 호출
    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 0, {arr[i][j]})

    return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    solve = dessert(N, arr)
    print(f'#{tc} {solve}')

# 2819 - 격자판 숫자 이어붙이기 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def solve(arr):
    result = set()
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(i, j, str(arr[i][j])) for i in range(4) for j in range(4)])

    while q:
        x, y, word = q.popleft()

        if len(word) == 7:
            result.add(word)
            continue

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, word + str(arr[nx][ny])))

    return len(result)

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    print(f'#{tc} {solve(arr)}')

# 1861 - 정사각형 방 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(n, arr):
    max_move = 0
    start_num = float('inf')

    for i in range(n):
        for j in range(n):
            q = deque([(i, j, arr[i][j], 1)])
            visited = {(i, j)}
            while q:
                x, y, now, cnt = q.popleft()

                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited and now + 1 == arr[nx][ny]:
                        q.append((nx, ny, arr[nx][ny], cnt + 1))
                        visited.add((nx, ny))

            if cnt > max_move:
                max_move = cnt
                start_num = arr[i][j]
            elif cnt == max_move:
                start_num = min(start_num, arr[i][j])

    return start_num, max_move


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    start_num, max_move = solve(n, arr)
    print(f'#{tc} {start_num} {max_move}')