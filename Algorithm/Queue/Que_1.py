# 미로
from collections import deque


def find(sx, sy, endx, endy, maze):
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 어떤 방향으로 탐색을 할 건지
    visited = [[False] * 16 for _ in range(16)] # visited를 사용하여 벽에서 막힐거임임

    for i in range(16): # 벽을 
        for j in range(16):
            if maze[i][j] == 1:
                visited[i][j] = False 

    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        print(x, y)

        if x == endx and y == endy:
            return 1

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                queue.append((nx, ny))
                visited[nx][ny] = True

    return 0

def route(maze):
    start_x = 0
    start_y = 0
    end_x, end_y = 0, 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
            elif maze[i][j] == 3:
                end_x = i
                end_y = j

    a = find(start_x, start_y, end_x, end_y, maze)

    return a

for i in range(1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{n} {route(maze)}')

# --------------------------------------------------------------------------
# 미로 while문 안에 종료 조건을 넣어서 바꾼 버전
from collections import deque


def find(sx, sy, endx, endy, maze):
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = [[False] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 1:
                visited[i][j] = False

    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if nx == endx and ny == endy:
                return 1

            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False and maze[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return 0

def route(maze):
    start_x = 0
    start_y = 0
    end_x, end_y = 0, 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
            elif maze[i][j] == 3:
                end_x = i
                end_y = j

    a = find(start_x, start_y, end_x, end_y, maze)

    return a

for i in range(1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{n} {route(maze)}')

# -----------------------------------------------------------------------------------
# 암호생성기
from collections import deque

def password(arr):
    cnt = 1
    while 0 not in arr:
        for _ in range(5):
            num = arr.popleft()
            num -= cnt
            if num <= 0:
                num = 0
                arr.append(num)
                break
            arr.append(num)
            cnt += 1
        cnt = 1

    return print(*arr)


for i in range(10):
    n = int(input())
    arr = deque(map(int, input().split()))
    print(f'#{n}', end = ' ')
    password(arr)