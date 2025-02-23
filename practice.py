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