import sys
from collections import deque
# sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\싸피\\for_py\\baekjoon\\2508\\input2508.txt", "r")
input = sys.stdin.readline

M, N = map(int, input().strip().split())
tomatos = [list(map(int, input().strip().split())) for _ in range(N)]

def solve(M, N, tomatos):
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque()
    answer = 0
        
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 1:
                q.append((i, j, 0))
    while q:
        x, y, day = q.popleft()
        
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = 1
                q.append((nx, ny, day + 1))
                answer = max(answer, day+1)
    
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                return -1
    
    return answer

print(solve(M, N, tomatos))