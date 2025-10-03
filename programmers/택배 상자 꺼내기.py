def solution(n, w, num):
    answer = 0
    h = n // w
    arr = [[0] * w for _ in range(h+1)]
    x, y = h, 0
    arr[x][y] = 1
    delta = [(0, 1), (0, -1)]
    direction = 0  # left = 1
    cnt = 2

    while cnt < n:
        for _ in range(w-1):
            if cnt < n:
                x = x + delta[direction][0]
                y = y + delta[direction][1]
                arr[x][y] = cnt
                cnt += 1

        if direction == 1:
            direction = 0
        else:
            direction = 1

        x -= 1
        arr[x][y] = cnt
        cnt += 1

    for i in range(h):
        for j in range(w):
            if arr[i][j] == num:
                ty = j
                break

    for i in range(h):
        if arr[i][ty] != 0:
            answer += 1

    return answer


print(solution(22, 6, 8))