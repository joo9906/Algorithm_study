import sys
input = sys.stdin.read

T = int(input())

def bomb():
    n, m = map(int, input().split())
    k = int(input())
    arr = [list(input()) for _ in range(n)]
    delta = [[0,1], [1, 0], [0, -1], [-1, 0]]

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                for x, y in delta:
                    nx = i + x
                    ny = j + y
                    long = 0
                    
                    while long < k:
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]== '_':                       
                            arr[nx][ny] = '%'
                            nx += x
                            ny += y
                            long += 1
                        else:
                            break
                arr[i][j] = '%'

    for k in range(n):
        print(''.join(arr[k]))

for p in range(1, T+1):
    print(f'#{p}')
    bomb()