import sys
from collections import deque
input = sys.stdin.readline
#sys.stdin = open('input.txt', 'r')

t = int(input().strip())
delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for _ in range(t):
    m, n, k = map(int, input().split())
    betchu = [[0] * m for _ in range(n)]
    check = [[False] * m for _ in range(n)]

    for _ in range(k):
        w, h = map(int, input().split())
        betchu[h][w] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if betchu[i][j] == 1 and not check[i][j]:
                ans += 1
                q = deque([(i, j)])
                check[i][j] = True

                while q:
                    y, x = q.popleft()
                    for dy, dx in delta:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m:
                            if betchu[ny][nx] == 1 and not check[ny][nx]:
                                check[ny][nx] = True
                                q.append((ny, nx))
    print(ans)