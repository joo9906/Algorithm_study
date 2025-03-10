from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())

class brick:

    def __init__(self, arr, N, W, H):
        self.arr = arr # 바뀌지 않을 맵(first에서 처음 들어갈 때 항상 얘로 받으면서 들어감)
        self.N = N # 최대 터트릴 수 있는 횟수
        self.W = W
        self.H = H
        self.max_cnt = 0
        self.total_brick = 0 # 총 벽돌의 개수
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    self.total_brick += 1

    def gravity(self, arr):
        for i in range(self.W):
            gh = self.H - 1
            for j in range(self.H-1, -1, -1): # 맨 아래~ 맨 위까지
                if arr[j][i] != 0:
                    arr[j][i], arr[gh][i] = arr[gh][i], arr[j][i]
                    gh -= 1
        return arr


    def bomb(self, arr, x, y, now_num, total, cnt):
        if cnt == self.N:
            if total > self.max_cnt:
                self.max_cnt = total
            return
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque([])
        bomb_block = 0

        if now_num == 1: # 구슬이 맞은 부분이 1이면 0으로 바꾸고 다음 구슬을 떨어트림
            arr[x][y] = 0
            total += 1
            cnt += 1
            self.drop(arr, cnt, total)


        elif arr[x][y] > 1: # 구슬이 맞은 부분이 1보다 크면 q에 넣어서 arr의 값들을 바꿔주는 베이스를 만들어 준다
            for dx, dy in delta: # 맨 처음 구슬과 연쇄로 터지는 블록들을 q에 넣는 부분
                for _ in range(now_num-1):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.H and 0 <= ny < self.W and arr[nx][ny] != 0:
                        q.append((arr[nx][ny], nx, ny)) # 터진 블록이 범위 안이고 0이 아니면 값과 좌표를 q에 넣어줌
                        bomb_block += 1
                        arr[nx][ny] = 0 # 넣은 값 부분은 arr에서 0으로 바꿈(다시 방문하면 안됨)

        while q:
            num, now_x, now_y = q.popleft()

            arr[now_x][now_y] = 0 # 뽑아온 현재 좌표를 0으로 바꿈

            bomb_block += 1

            for dx, dy in delta: # 뽑아온 블록의 값이 1보다 크면 델타를 돌면서 또 터트릴 수 있는 블록을 넣음
                for _ in range(num-1):
                    nx = now_x + dx
                    ny = now_y + dy
                    if 0 <= nx <= self.H and 0 <= ny <= self.W and arr[nx][ny] != 0:
                        q.append((arr[nx][ny], nx, ny))
                        bomb_block += 1
                        arr[nx][ny] = 0

        narr = self.gravity(arr)
        self.drop(narr, total + bomb_block, cnt + 1) # 위에서 다 터트리고 정렬 된 arr을 drop에 넣어서 맨 위부터 또 떨어트림. cnt와 bomb-block는 공유


    def drop(self, arr, total, cnt): # 구슬을 떨어뜨리는 부분
        if cnt == self.N:
            return
        top = deque([(0, i) for i in range(self.W)])
        q = deque([])

        while top: # 맨 윗줄에서 모두 다 떨어트려본다
            start_x, start_y = top.popleft() # 시작하는 row(x가 0~9까지)
            while start_x < self.H and arr[start_x][start_y] == 0: # 0이 아닌 점을 만날 때 까지
                start_x += 1
            if start_x < self.H:
                q.append((arr[start_x][start_y], start_x, start_y)) # 0이 아닌 지점을 만나면 q에 넣어서 한 줄의 시작을 알림

        while q:
            tn, x, y = q.popleft()

            self.bomb(self.arr, x, y, tn, total, cnt) # 맨 처음에는 가장 위에서 떨어트리는 경우니까 0,i (i = 0 ~ W-1)

    def result(self):
        return self.total_brick - self.max_cnt

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().strip().split())) for _ in range(H)]
    solve = brick(arr, N, W, H)
    solve.drop(arr, 0, 0)

    print(f'#{tc} {solve.result()}')