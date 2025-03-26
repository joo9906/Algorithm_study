# 스위치 켜고 끄기
def turn(arr, n): # 해당 스위치의 상태를 바꾸는 함수
    if arr[n] == 0:
        arr[n] = 1
    elif arr[n] == 1:
        arr[n] = 0

def boy(arr, num, n): # 남자일 때 적용
    for i in range(num-1, len(arr), num): # 받은 위치의 배수번째 위치의 스위치를 turn 함
        turn(arr, i)

def girl(arr, num, find): # 여자일 때 적용
    if num - find < 0 or num + find >= len(arr) or arr[num - find] != arr[num + find]:
        return turn(arr, num)
    elif arr[num-find] == arr[num+find]:
        turn(arr, num-find)
        turn(arr, num+find)
        girl(arr, num, find+1)

def off(): # input 값들을 받고 실행한 뒤 출력까지 하는 함수
    n = int(input())
    arr = list(map(int, input().split()))
    head = int(input())
    people = [list(map(int, input().split())) for _ in range(head)]

    for x, y in people: #남/여 받은대로 실행
        if x == 1:
            boy(arr, y, n)
        elif x == 2:
            girl(arr, y-1, 1)

    cnt = 0
    for i in arr:
        print(i, end=' ')
        cnt += 1
        if cnt == 20:
            print()
            cnt = 0

off()

# -------------------------------------------------------------------------

# 나이트의 이동 - 월말 형식(덱 못쓴다고 해서 만든거)
T = int(input())

def chess():
    I = int(input())
    arr = [[0] * I for _ in range(I)] # 체스판 생성
    start_x, start_y = map(int, input().split())  # 나이트가 시작하는 좌표
    target_x, target_y = map(int, input().split()) # 도달해야 할 좌표
    
    # 시작점과 목표점이 같으면 바로 중단
    if start_x == target_x and start_y == target_y: 
        return 0
    
    # 나이트가 이동할 수 있는 칸의 델타 - 순서대로 1시 2시 4시 5시 7시 8시 10시 11시 방향
    delta = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    
    q = [(start_x, start_y, 0)] #현재 x좌표와 y좌표, 움직인 횟수 / 이후에는 움직인 좌표들이 들어갈거임
    
    # 타겟과 시작점이 같은 경우 꼬이면 안되니까 타겟을 시작점보다 나중에 지정해줘야 함
    arr[start_x][start_y] = 1 # 시작점의 좌표를 1로 바꾸고 시작(방문 했다는 표시)
    arr[target_x][target_y] = 2  # 나이트가 도착하려는 좌표를 2로 설정
    
    
    
    while q: # q에 저장하는 값이 있는동안 계속 반복(없으면 못 가는 것이므로 중단)
        now_x, now_y, cnt = q.pop(0) # x, y 좌표들을 받고 cnt는 움직인 횟수 / 가장 왼쪽을 뽑아야 함

        for x, y in delta: # 델타를 순회하며 나이트가 움직일 수 있는 좌표를 탐색
            nx = now_x + x # 다음 x좌표
            ny = now_y + y # 다음 y좌표
            
            
            
            # 체스판을 벗어나지 않고 다음 좌표가 방문한 곳도 아니라면 실행
            if 0 <= nx < I and 0 <= ny < I and arr[nx][ny] != 1:
                if arr[nx][ny] == 2: # 다음 좌표가 목적지라면 cnt에 1 더하고 끝
                    return cnt + 1
            
                q.append((nx, ny, cnt + 1)) # 좌표 저장소에 다음 좌표를 저장
                arr[nx][ny] = 1 # 다음 좌표를 방문했다고 표시 함
    
    return 'Fail'
         
for k in range(T):
    print(chess())
    
# --------------------------------------
# 미로 탐색

def maze():
    ty, tx = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(ty)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)] #시계방향 델타
    arr[0][0] = 0 # 첫 좌표 방문처리
    
    q = [(0, 0, 1)] # 첫 좌표도 1회로 쳐서 시작
    
    while q: # q에 값이 있는동안 계속 반복
        nowy, nowx, cnt = q.pop(0) # q의 왼쪽 끝을 꺼내서 현재의 y, x좌표, 움직인 횟수를 뽑아옴

        if nowy == ty-1 and nowx == tx-1: # 현재의 y좌표, x좌표가 목표점과 같으면 cnt 뱉음
            return cnt
        
        for dy, dx in delta: # 델타를 돌면서 dy와 dx 값을 받음
            nx = nowx + dx # 다음 x좌표는 nowx + dx
            ny = nowy + dy # 다음 y 좌표는 nowy + dy

            # 미로 내에 있고 다음 좌표가 1일 때
            if 0 <= ny < ty and 0 <= nx < tx and arr[ny][nx] == 1:
                q.append((ny, nx, cnt + 1)) # 다음 y좌표, 다음 x좌표, 이동 횟수에는 1 추가
                
                # 여기서 먼저 0 처리를 해줘야 for문을 돌면서 불필요한 좌표를 변경하지 않음
                arr[ny][nx] = 0 
print(maze())
