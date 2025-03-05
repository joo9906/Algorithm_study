import sys
from collections import deque
input = sys.stdin.readline

def maze():
    n, m = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    
    q = deque([(0, 0, 1)])

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == n-1 and y == m-1:
            return cnt
        
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                q.append((nx, ny, cnt + 1))
                arr[nx][ny] = 0

print(maze())