T = int(input())
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def search(x, y, cnt):
    num = []
    direction = []
    for delta_x, delta_y in delta:
        dx = x + delta_x
        dy = y + delta_y
        if 0 <= dx < n and 0 <= dy < n:
            direction.append([dx, dy])
            num.append(arr[dx][dy])

    a = num.index(min(num))
    dx, dy = direction[a]

    if 0 <= dx < n and 0 <= dy < n and arr[x][y] > arr[dx][dy]:
        search(dx, dy, cnt+1)
        return
    else:
        result.append(cnt)


def ball(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            search(i, j, cnt)


for i in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    ball(n)
    print(f'#{i} {max(result)}')