# 2589번 - 보물섬
import sys
from collections import deque
input = sys.stdin.readline

def solve(h, w, array):
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    start_point = set()
    weight_map = [([0] * w) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if array[i][j] == 'L':
                start_point.add((i, j))

    for pos in start_point:
        visited = [([False] * w) for _ in range(h)]

        q = deque([(0, pos[0], pos[1])])
        visited[pos[0]][pos[1]] = True

        while q:
            weight, x, y = q.popleft()
            weight_map[x][y] = max(weight_map[x][y], weight)

            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and array[nx][ny] != 'W' and visited[nx][ny] == False:
                    q.append((weight+1, nx, ny))
                    visited[nx][ny] = True
    
    answer = 0
    for a in range(w):
        for b in range(h):
            answer = max(answer, weight_map[b][a])

    return answer

H, W = map(int, input().strip().split())
array = [list(map(str, input().strip())) for _ in range(H)]
print(solve(H, W, array))

# ---------------------------------------------------------------------------------------------------------