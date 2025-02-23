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

# ---------------------------------------------------------------
# 톱니바퀴 좀 무식하게 푼 거
saw = [None] + [deque(map(int, input())) for _ in range(4)]

roll = int(input())
turn = deque()

for i in range(roll):
    n, m = map(int, input().split())
    turn.append((n, m))

def turn_clock(num):
    saw[num].appendleft(saw[num].pop())
    
def turn_counter(num):
    saw[num].append(saw[num].popleft())

def turn_func(saw, roll, turn):
    for _ in range(roll):
        num, direct = turn.popleft()
        
        if direct == 1:
            if num == 1:
                if saw[1][2] != saw[2][6]:
                    if saw[2][2] != saw[3][6]:
                        if saw[3][2] != saw[4][6]:
                            turn_counter(4)
                        turn_clock(3)
                    turn_counter(2)
                turn_clock(1)
                
            elif num == 2:
                if saw[1][2] != saw[2][6]:
                    turn_counter(1)
                    
                if saw[2][2] != saw[3][6]:
                    if saw[3][2] != saw[4][6]:
                        turn_clock(4)
                    turn_counter(3)
                turn_clock(2)
            
            elif num == 3:
                if saw[3][2] != saw [4][6]:
                    turn_counter(4)
                
                if saw[3][6] != saw[2][2]:
                    if saw[1][2] != saw[2][6]:
                        turn_clock(1)
                    turn_counter(2)
            
            elif num == 4:
                if saw[4][6] != saw[3][2]:
                    if saw[3][6] != saw[2][2]:
                        if saw[2][6] != saw[1][2]:
                            turn_counter(1)
                        turn_clock(2)
                    turn_counter(3)
                turn_clock(4)
        
        elif direct == -1:
            if num == 1:
                if saw[1][2] != saw[2][6]:
                    if saw[2][2] != saw[3][6]:
                        if saw[3][2] != saw[4][6]:
                            turn_clock(4)
                        turn_counter(3)
                    turn_clock(2)
                turn_counter(1)
                
            elif num == 2:
                if saw[1][2] != saw[2][6]:
                    turn_clock(1)
                    
                if saw[2][2] != saw[3][6]:
                    if saw[3][2] != saw[4][6]:
                        turn_counter(4)
                    turn_clock(3)
                turn_counter(2)
            
            elif num == 3:
                if saw[3][2] != saw[4][6]:
                    turn_clock(4)
                
                if saw[3][6] != saw[2][2]:
                    if saw[1][2] != saw[2][6]:
                        turn_counter(1)
                    turn_clock(2)
                turn_counter(3)
            
            elif num == 4:
                if saw[4][6] != saw[3][2]:
                    if saw[3][6] != saw[2][2]:
                        if saw[2][6] != saw[1][2]:
                            turn_clock(1)
                        turn_counter(2)
                    turn_clock(3)
                turn_counter(4)
            
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
    
    return cnt

print(turn_func(saw, roll, turn))

# -----------------------------------------------------------------
# 주사위 굴리기

# from collections import deque

N, M, start_x, start_y, K = map(int, input().split())
jido = [list(map(int, input().split())) for _ in range(N)]
comp = deque(list(map(int, input().split()))) #선입선출 할거니까 popleft 쓰려고 deque으로 받음

# 1 2 3 4로 방위를 받으니 그 순서대로 동 서 북 남 delta를 설정
delta = [[None], [0,1], [0, -1], [-1, 0], [1, 0]] 
dice = [0] * 7 # 주사위 6면(0은 어차피 안쓰니까 인덱스로 쓰려고)
num = 6 # 얘는 저 밑에 코드를 다 짜고 뒤늦게 발견해서 안고친거임... num 들어간 부분 다 6으로 써도 됨

# dicing 함수는 방위를 받고 그걸 기준으로 바뀌는 주사위의 면들을 첫 전개도로 고정시킴
# 뭐라고 해야하나... 주사위를 굴리는걸 표현한건데 동서남북으로 주사위를 굴렸을 때
# 1번 자리에 4번이 오고 6번 자리에 3번이 오고..... 하는 것들을 표현 해준 것
# 그림 그려서 해보면 더 편하게 지정 가능할 듯 합니다..
# 그냥 뇌로 되면 제발 뇌 이식 좀. 전 능지 딸려서 안됨

def dicing(direction):
    global dice 
    # 이놈을 global로 안받으면 밑부분이 지들끼리 북치고 장구쳐서 dice에
    # 하나도 반영이 안됩니다. 어떻게 알았냐구요? 묻지 마쇼.
    
    if direction == 1:
        dice[1], dice[6], dice[3], dice[4]  = dice[4], dice[3], dice[1], dice[6]
        
    elif direction == 2:
        dice[1], dice[6], dice[3], dice[4]  = dice[3], dice[4], dice[6], dice[1]
        
    elif direction == 3: 
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
        
    elif direction == 4: # 여기서 숫자 바꿔 써서 3번 실패함... 설정 잘 하세요...ㅎ...
        dice[1], dice[2], dice[5], dice[6],  = dice[2], dice[6], dice[1], dice[5]
        
    
while comp: # 방향 전환을 받아온 만큼 실행(for문으로 쓰면 K번 반복하면 됨)
    direction = comp.popleft() # 선입선출로 방향을 comp에서 뽑아옴
    dx, dy = delta[direction]  # 델타의 direction번째에서 dx와 dy를 뽑아옴
    nx = start_x + dx # nx = 굴러간 x 좌표
    ny = start_y + dy # ny = 굴러간 y 좌표

    if 0 <= nx < N and 0 <= ny < M: # 굴린 다음 지도 안에 있어야 실행이니까
        dicing(direction)

        if jido[nx][ny] == 0: #지도의 nx, ny 좌표가 0이면 지도에 dice[6]의 숫자를 입력
            jido[nx][ny] = dice[num]
            
        else: # 지도의 nx, ny 좌표가 0이 아니면 dice[6]에 지도의 숫자를 입력
            dice[num] = jido[nx][ny]
            jido[nx][ny] = 0 # dice에 입력 했으면 해당 좌표 지도의 숫자는 0으로 바꿈
        
        # dicing 함수에서 1은 무조건 위로 오게끔 만들어 뒀으므로 1만 출력하면 됨
        print(dice[1]) 
        start_x, start_y = nx, ny # 다 끝난 다음 x, y좌표를 바꿔줌

# ------------------------------------------------------------------
# 로봇청소기
N, M = map(int, input().split())
r, c, d = map(int, input().split()) # (r, c)가 로봇 청소기의 첫 좌표, d는 첫 방향
arr = [list(map(int, input().split())) for _ in range(N)]
delta = [[-1, 0], [0, 1],  [1, 0], [0, -1]] # 북동남서 순서(문제에서 주어진 방향 순서대로)
check_point = 0

def find(r, c):
    for x, y in delta:  # 지금 좌표 기준으로 시계방향 탐색
        nx = x + r
        ny = y + c
        if arr[nx][ny] != 1 and arr[nx][ny] != 2: # 다음 좌표가 벽이나 청소된 곳이 아니라면
            return True
    return False

# 0은 청소 가능한 곳, 1은 벽, 2는 이미 청소한 곳
def cleaning():
    global r, c, check_point

    turn_point = d  # 델타에서 받아올 방향의 index
    cnt = 0 # 몇 칸이나 청소 했는지
    nx = r # 시작점의 x 좌표
    ny = c # 시작점의 y 좌표

    while True:
        if arr[nx][ny] == 0:  # 현재 좌표의 값이 0이면 그 칸 청소
            cnt += 1
            arr[nx][ny] = 2   # 청소 했으니 2로 표시

        if not find(nx, ny):  # find를 해서 바꿀 수 있는 곳이 없으면 후진
            x, y = delta[turn_point] # 후진하기 위해 현재 바라보고 있는 곳의 델타를 받아옴
            if arr[nx-x][ny-y] == 1:  # 후진이 벽 때문에 불가능하면 작동을 멈춤
                return cnt
            else:  # 벽만 아니면 후진
                nx -= x
                ny -= y

        else: # 갈 수 있는 곳이 하나라도 있으면 반시계 방향으로 90도 돌면서 실행
            for _ in range(4):
                turn_point = (turn_point -1) % 4 # 첫 시작은 받아온 방향의 반시계 90도, 계속 값을 바꿔가며 사방을 찾음
                x, y = delta[turn_point]
                if arr[nx+x][ny+y] == 0:  # 갈 수 있다면 nx값과 ny값을 바꾸고 while문 탈출
                    nx += x
                    ny += y
                    break

print(cleaning())

