import math

def solution(n, w, num):
    h = math.ceil(n / w)  # 전체 층 수
    arr = [[0] * w for _ in range(h)]
    x, y = h - 1, 0  # 시작점 (맨 아래 왼쪽)
    arr[x][y] = 1
    delta = [(0, 1), (0, -1)]
    direction = 0  # 0=오른쪽, 1=왼쪽
    cnt = 2

    if w == 1:  # 1줄짜리
        return n - num + 1

    while cnt <= n:
        # 한 줄 채우기
        for _ in range(w - 1):
            if cnt > n:
                break
            x = x + delta[direction][0]
            y = y + delta[direction][1]
            arr[x][y] = cnt
            cnt += 1

        # 위로 올라가기
        x -= 1
        if cnt <= n:
            arr[x][y] = cnt
            cnt += 1

        # 방향 반전
        direction = 1 - direction

    # num 위치 찾기
    ty = None
    for i in range(h):
        for j in range(w):
            if arr[i][j] == num:
                ty = j
                break
        if ty is not None:
            break

    # 세로줄 박스 개수
    answer = 0
    for i in range(h):
        if arr[i][ty] != 0:
            answer += 1

    return answer
