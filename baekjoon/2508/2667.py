import sys
from copy import deepcopy
from collections import deque
#input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

t = int(input().strip())
apart = [list(map(int, input().strip())) for _ in range(t)]

def solve(x, y):
    global t, apart, visited
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while q:
        sx, sy= q.popleft()
        
        for dx, dy in delta:
            nx = sx + dx
            ny = sy + dy
            if 0 <= nx < t and 0 <= ny < t and visited[nx][ny] == False and apart[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    
    return cnt
        
answer = []
visited = [[False] * t for _ in range(t)]

for i in range(t):
    for j in range(t):
        if apart[i][j] == 1 and visited[i][j] == False:
            app = solve(i, j)
            answer.append(app)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)