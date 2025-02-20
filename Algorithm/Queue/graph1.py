# 방문 순서 출력하기
from collections import deque
q = deque([])

T = int(input())

for i in range(1, T+1):
    n = int(input())
    print(f'#{i}', end = ' ')

    arr = [list(map(int, input().split())) for _ in range(n)]
    bfs = [deque() for _ in range(n)]
    visited = [False] * (n+1)
    q = deque()
    start = 0
    visited[start] = True
    q.append(start)
    print(start, end = ' ')


    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                bfs[i].append(j)

    while q:
        node = q.popleft()
        while bfs[node]:
            target = bfs[node].popleft()
            if visited[target] == False:
                q.append(target)
                visited[target] = True
                print(target, end=' ')

    print()

# ------------------------------------------------------------------------------------------
# 경로 출력하기
from collections import deque


T = int(input())

for i in range(1, T+1):
    n = int(input())
    print(f'#{i}')

    arr = [list(map(int, input().split())) for _ in range(n)] # 인접행렬 정보
    bfs = [deque() for _ in range(n)] # bfs를 n만큼의 deque로 구성
    visited = [False] * (n+1) # 방문했다는 정보

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                bfs[i].append(j)

    q = deque([0])  # 출력할 덱, 시작을 무조건 0으로 할거임
    node = q[0]
    visited[node] = True# 0이 두번 안들어가게끔 방문했다고 표시

    while bfs[node]:
        target = bfs[node].popleft()
        q.append(target)
        visited[target] = True
        while bfs[target]:
            last_target = bfs[target].popleft()
            if visited[last_target] == False:
                q.append(last_target)
                visited[last_target] = True
                print(*q)
                q.pop()
        q.pop()
