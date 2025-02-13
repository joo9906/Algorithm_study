T = int(input())
 
def bomb():
    n, m = map(int, input().split())
    k = int(input())
    arr = [list(input()) for _ in range(n)]
    delta = [[0,1], [1, 0], [0, -1], [-1, 0]]
 
    for i in range(n):
        for j in range(m):
            for x, y in delta:
                nx = i + x
                ny = j + y
                if 0 <= nx < n and 0 <= ny < m and arr[i][j] == '@':
                    for _ in range(k):
                        if arr[nx][ny] == '_':
                            arr[nx][ny] = '%'
                            nx += x
                            ny += y
                        else:
                            break
            if arr[i][j] == '@':
                arr[i][j] = '%'
 
    for k in range(n):
        print(''.join(arr[k]))
 
for p in range(1, T+1):
    print(f'#{p}')
    bomb()

폭탄테러 - 테스트 5개 다 맞았다면서 런타임에러 떴음