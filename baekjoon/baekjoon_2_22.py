# 뱀 - 3190번
from collections import deque

N = int(input())
k = int(input())
arr = [[0] * N for _ in range(N)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 5 

L = int(input()) 
direction = deque()

for _ in range(L):
    sec, direc = input().split()
    direction.append((int(sec), direc))

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 오른쪽, 아래, 왼쪽, 위
delta_index = 0  # 처음엔 오른쪽

def snake():
    global delta
    global delta_index
    
    nx, ny = 0, 0  # 뱀 머리 위치 (처음엔 0, 0에서 시작)
    arr[nx][ny] = 1  # 뱀이 있는 곳은 1(계속 1로 만들거 아니고 지나가면 0으로 만들어야함)
    body = deque([(nx, ny)])  # 뱀의 몸 저장(arr에선 몸통이 있는 부분도 1로 만들거임)
    cnt = 0 

    while True:
        cnt += 1
        dx, dy = delta[delta_index]  # 현재 이동 방향
        nx, ny = nx + dx, ny + dy  # 다음 위치 이동

        # 벽 또는 자기 자신과 충돌하면 종료
        if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] == 1:
            return cnt

        # 사과가 있으면 길이 유지(원래 1에서 2로 늘어나는 것), 없으면 몸통 끝 제거
        if arr[nx][ny] == 5:
            arr[nx][ny] = 0  # 사과 먹으면 해당 좌표 0으로 바꿈
        else:
            tail_x, tail_y = body.popleft()  # 꼬리 제거
            arr[tail_x][tail_y] = 0  # 꼬리 자리 비우기

        arr[nx][ny] = 1 # 다음 머리 위치로 이동
        body.append((nx, ny))

        # 방향 전환이 있는 경우 - 이거 8초뒤, 10초뒤가 아니라 총 시간이 8초 지나면, 10초 지나면임
        # 그니까 2번 케이스에서 총 시간(cnt)이 8초가 되면 D로 바꾸고 10초가 되면 D로 바꾸는 식
        # 나는 8초 후 D, 10초 후 D로 생각해서 8초, 18초에 방향을 바꾸고 있었음
        if direction and direction[0][0] == cnt:
            t, turn = direction.popleft()
            if turn == 'D':  # 오른쪽 회전
                delta_index = (delta_index + 1) % 4
            else:            # 왼쪽 회전
                delta_index = (delta_index - 1) % 4

print(snake())

# -------------------------------------------------------------------------------
# 톱니바퀴

saw = [None] + [deque(map(int, input())) for _ in range(4)]

roll = int(input())
turn = [tuple(map(int, input().split())) for _ in range(roll)]

# 시계 방향 회전
def turn_clock(num):
    saw[num].appendleft(saw[num].pop())

# 반시계 방향 회전
def turn_counter(num):
    saw[num].append(saw[num].popleft())

def turn_func():
    for num, direct in turn:
        rotate = [0] * 5  # 톱니 번호는 1부터 시작하니까 5개로 만들어서 0 남김
        rotate[num] = direct  # 해당 톱니바퀴의 회전 방향 기록

        # num번째 톱니 기준 왼쪽 확인
        for i in range(num, 1, -1):
            if saw[i][6] != saw[i - 1][2]:  # 맞닿은 톱니가 다르면 반대 방향 회전
                rotate[i - 1] = -rotate[i]  # 시계/반시계가 1, -1이니까 그 뜻
            else:
                break

        # nu번째 톱니 기준 오른쪽 확인
        for i in range(num, 4):
            if saw[i][2] != saw[i + 1][6]:
                rotate[i + 1] = -rotate[i]
            else:
                break

        for i in range(1, 5):
            if rotate[i] == 1: #시계방향 회전
                turn_clock(i)
            elif rotate[i] == -1: # 반시계방향 회전
                turn_counter(i)

    cnt = 0
    for i in range(1, 5):
        if saw[i][0] == 1:
            if i == 1:
                cnt +=1
            elif i == 2:
                cnt +=2
            elif i == 3:
                cnt += 4
            elif i == 4:
                cnt += 8

print(turn_func())