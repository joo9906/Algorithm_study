# n = int(input())

def check(x, y):
    global n

    delta = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    ans = True

    for dx, dy in delta:
        nx = x + dx
        ny = y + dy
        while 0 <= nx < n and 0 <= ny < n:
            pass
            

def solve(n):
    chess_map = [[0] * n] * n
    


n = 8
solve(n)