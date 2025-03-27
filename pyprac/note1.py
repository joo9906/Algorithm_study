import sys, heapq
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(n, idx):
    global result, height

    if n >= result:
        return

    if n >= b:
        result = min(n, result)
        return

    for i in range(idx, len(height)):
        if not visited[i]:
            visited[i] = True
            solve(n+height[i], i)
            visited[i] = False

T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    visited = [False] * n
    result=float('inf')
    solve(0, 0)
    print(f'#{tc} {result - b}')
