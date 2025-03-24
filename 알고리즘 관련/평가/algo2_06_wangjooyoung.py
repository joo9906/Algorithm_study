T = int(input())

def monster():
    n = int(input())
    arr = [list(map(int, input())) for _ in range(10)]
    delta = [[0,1], [1, 0], [0, -1], [-1, 0]] #오른쪽, 아래, 왼쪽, 위를 탐색하기 위해 델타 설정
    kind = [1, 2, 3, 4] #괴물과 벽인지 확인하기 위해
    cnt = 0
    visited = [[0] * 10 for _ in range(10)]

    for i in range(10): # 괴물의 위치를 3으로 지정
        for j in range(10):
            if arr[i][j] in kind:
                visited[i][j] = 3

    for i in range(10): # arr을 전체 탐색
        for j in range(10):
            if arr[i][j] == 0 or arr[i][j] == 4: #해당 좌표가 0이거나 벽이면 아무것도 하지 않고 넘어감
                continue
            else:
                for x, y in delta: # arr[i][j] 좌표를 중심으로 상하좌우의 값을 nx, ny좌표로 설정
                    nx = x + i
                    ny = y + j
                    if visited[i][j] == 3: # arr[i][j]가 괴물이면 아래의 코드 실행
                        for _ in range(arr[i][j]):  # 괴물의 숫자 만큼 상하좌우의 칸을 바꿈
                            if 0 <= nx < 10 and 0 <= ny < 10 :
                                if visited[nx][ny] == 3: # arr[nx][ny]값을 1로 바꿀건데 그 자리에 괴물이 있으면 바꾸지 않음
                                    continue
                                else:
                                    visited[nx][ny] = 1 #괴물도 아니고 벽도 아니면 해당 좌표에 방문했다고 visit의 값을 바꿈
                                    arr[nx][ny] = 1 # 광선이 닿는 범위로 바꿈
                                    nx += x
                                    ny += y
    print(arr)
    for i in range(10): # 전체 배열에서 사람이 살 수 있는 0만 탐색
        for j in range(10):
            if arr[i][j] == 0:
                cnt += 1

    return cnt

for k in range(1, T+1):
    print(f'#{k} {monster()}')