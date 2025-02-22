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
# ------------------------------------------------------------------------
# 바이러스 - DFS
from collections import deque
 
T = int(input())
 
for nums in range(1, T+1):
    com_num = int(input())
    line = int(input())
    visited = [False] * (com_num+1)
    start = 1
    cnt = 0
 
    inj = [deque() for _ in range(com_num+1)]
 
    for i in range(line): # 컴퓨터들이 몇 번 컴퓨터랑 연결되어 있는지 확인
        n, m = map(int, input().split())
        inj[n].append(m)
        inj[m].append(n)
         
    def virus(start): # 1번과 연결된 컴퓨터면 visited를 True로 바꾸는 함수(재귀)
        while inj[start]:
            node = inj[start].popleft()
            visited[node] = True
            virus(node)
 
    virus(start)
    result = visited.count(True)
         
 
    print(f'#{nums} {result-1}')

# ----------------------------------------------------------------------------
# 상사와 부하
from collections import deque
 
T = int(input())
 
def find(start, under): 
    while inj[start]:
        node = inj[start].popleft()
        under.append(node)
        visited[node] = True
        find(node, under)
    return under
 
for nums in range(1, T+1):
    people = int(input())
    visited = [False] * (people)
    start = 0
    under = []
    boss = 0
    inj = [deque() for _ in range(people)]
 
    arr = [list(map(int, input().split())) for _ in range(people)] 
     
    for i in range(people): # 누가 누구랑 연결되어있는지 arr을 순회하며 찾음
        for j in range(people):
            if arr[i][j] == 1:
                inj[i].append(j)
                 
    for k in range(len(inj)):
            if 0 in inj[k]:
                boss = k
 
    print(f'#{nums} boss:{boss} / under:', end = '')
    print(*find(start, under))
