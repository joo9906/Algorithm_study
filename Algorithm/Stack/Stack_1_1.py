# 방문 순서 출력하기
T = int(input())

def recur(arr, v, visit):
    visit[v] = 4 # 방문 여부를 알기 위해 가장 첫 방문은 했다(4라는 값으로) 설정
    print(v, end=' ') # v의 값을 출력

    for i in range(len(arr)): # 인접행렬의 줄 수 만큼 반복(첫 줄에서 제일 먼저 만나는 애부터 시작)
        if arr[v][i] == 1 and visit[i] == 3: # 첫번째 노드의 자식 노드들을 순회하면서 (v, i)에 간선이 있고, 방문도 하지 않았다(==3)면 해당 i값을 재귀하며 탐색
            recur(arr, i, visit)



for i in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = 0
    visit = [3] * N
    print(f'#{i+1}', end = ' ')
    recur(arr, v, visit)
    print()

# --------------------------------------------------------------------
# 괄호 짝짓기
for i in range(10):
    n = int(input())
    arr = list(input())
    test_case = []
    result = 1
 
    for j in range(len(arr)):
        ch = arr[j]
 
        if ch in ['{', '[', '(', '<']:
            test_case.append(ch)
 
        # elif i == ('}' or ']' or ')' or '>'):
        elif ch == '}':
            if test_case and test_case.pop() == '{':  # 비어있지 않고 짝이 맞으면
                continue
            else:
                result = 0  # 짝 안 맞으면 실패
                break
 
        elif ch == ']':
            if test_case and test_case.pop() == '[':
                continue
            else:
                result = 0
                break
 
        elif ch == ')':
            if test_case and test_case.pop() == '(':
                continue
            else:
                result = 0
                break
 
        elif ch == '>':
            if test_case and test_case.pop() == '<':
                continue
            else:
                result = 0
                break
 
    if test_case :
        result = 0
 
    print(f'#{i+1} {result}')

# -----------------------------------------------------------------------
# 길 찾기 - BFS를 사용해서 노드에 값들을 배정하고 하나씩 찾아가는 거
from collections import deque
 
def find_path(arr):
    # 0부터 99까지의 경로를 저장할 그래프
    graph = {i: [] for i in range(100)}
 
    for i in range(0, len(arr), 2):
        start, end = arr[i], arr[i+1]
        graph[start].append(end)
     
    # 경로 탐색
    queue = deque([0])  # 출발점 0부터 시작
    visited = [False] * 100  # 방문 기록
    visited[0] = True  # 출발점은 이미 방문
     
    while queue:
        current = queue.popleft()  # 큐에서 현재 정점 꺼내기
         
        if current == 99:  # 도착점 99에 도달하면 1
            return 1
         
        for neighbor in graph[current]:
            if not visited[neighbor]:  # 아직 방문하지 않은 노드라면
                visited[neighbor] = True
                queue.append(neighbor)
     
    # 도착 못하면 0
    return 0
 
 
for e in range(10):
    n, m = map(int, input().split()) 
    arr = list(map(int, input().split())) 
     
    result = find_path(arr)
    print(f'#{e+1} {result}')