#1987 - 알파벳
import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    start_char = arr[0][0]
    q.append((0, 0, set([start_char]), 1))

    max_count = 1
    visited = set()
    visited.add((0, 0, start_char))

    while q:
        x, y, used, count = q.popleft()
        max_count = max(max_count, count)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                char = arr[nx][ny]
                if char not in used:
                    new_used = used.copy()
                    new_used.add(char)

                    # visited 상태를 (좌표, 지금까지 사용한 알파벳 문자열) 로 관리
                    key = (nx, ny, ''.join(sorted(new_used)))
                    if key not in visited:
                        visited.add(key)
                        q.append((nx, ny, new_used, count + 1))

    return max_count

print(bfs())

# -----------------------------------------------------
