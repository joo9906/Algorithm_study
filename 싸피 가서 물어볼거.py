from collections import deque

T = int(input())
delta = [(0, 1), (1, 0)] # 우, 하 - 인덱스를 방향전환으로 쓸거임. 우회전만 가능하니까 다른 델타는 필요없음음

#실제로 다음 순서의 사과를 찾고 거기까지 필요한 우회전을 찾는 함수
def find(n, arr, start, target):
    # q에서 꺼내면서 최적 경로 탐색 할 것것
    q = deque()
    # 방문한 곳은 다시 안갈거니까(대신 다음 사과를 찾을 땐 상관 없이 방문 할거니까 find 안에 넣어서 항상 초기화)
    visited = set()
    
    # 시작하는 좌표를 q에 넣음
    q.append((start[1], start[0], 0, 0))
    # 시작하는 좌표와 우회전 횟수를 넣음
    visited.add((start[1], start[0], 0))

    # q가 비어있지 않는 동안 계속 반복
    while q:
        x, y, direct, turn = q.popleft()

        # 찾으려는 사과에 도착했으면 우회전 횟수를 반환하고 함수 종료
        if (y, x) == target:
            return turn
        
        # 전진하는 경우
        ny = y + delta[direct][0]
        nx = x + delta[direct][1]
        if 0 <= nx < n and 0 <= ny < n and (nx, ny, direct) not in visited:
            visited.add((nx, ny, direct))
            q.append((nx, ny, direct, turn))

        # 우회전 하는 경우
        newdirect = (direct + 1) % 2
        nx = x + delta[newdirect][1]
        ny = y + delta[newdirect][0]
        if 0 <= nx < n and 0 <= ny < n and (nx, ny, newdirect) not in visited:
            visited.add((nx, ny, newdirect))
            q.append((nx, ny, newdirect, turn+1))



# 문제 해결에 필요한 조건들을 지정하는 함수
def apple(n, arr):
    # 사과 위치를 찾아서 저장
    apple = {}
    for y in range(n): # 사과의 y좌표
        for x in range(n): # 사과의 x좌표
            if arr[y][x] != 0: # apple에 1번, 2번, 3번... 사과의 좌표를 딕셔너리로 받아 둠(list로 하면 앞에 빈 리스트 하나 넣고 하면 됨)
                apple[arr[y][x]] = (y, x)
    
    cnt = 0
    start = (0, 0)
    for i in range(1, len(apple)+1):
        target = apple[i] # i번 사과를 타겟으로 설정
        cnt += find(n, arr, start, target) # 시작점과 목표점을 받아 실행
        start = target # 찾고 나왔으면 시작점을 바꿔주고 다음 for문 실행행
    
    return cnt



for k in range(1, T +1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{k} {apple(n, arr)}')