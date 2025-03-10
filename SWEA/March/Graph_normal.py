# 시우의 이사
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


T = int(input())

def bus(N, Route, K, R):
    Node = {i:[] for i in range(1, N + 1)}
    result = set() # 방문 가능한 노드를 저장할 리스트

    for start, end in Route:
        Node[start].append(end)
        Node[end].append(start)

    q = deque([(0, K)])

    while q:
        cnt, next_node = q.popleft()

        if cnt > R: # cnt가 R보다 크면 정지
            break

        result.add(next_node)

        for j in Node[next_node]:
            q.append((cnt + 1, j))

    return len(result)


for tc in range(1, T+1):
    N, M = map(int, input().split())
    Route = [tuple(map(int, input().split())) for _ in range(M)]
    K, R = map(int, input().split())
    print(f'#{tc} {bus(N, Route, K, R)}')

# 초능력자 영기 ---------------------------------------------------------------------------
T = int(input())

def route(start, end):
    q = deque([(start, 0)])
    visited = [False] * 100001

    while q:
        now, cnt = q.popleft()
        move = [now - 1, now + 1, now * 2]
        if now == end:
            return cnt

        for x in move:
            if 0 <= x < 100001 and visited[x] != True:
                visited[x] = True
                q.append((x, cnt + 1))


for i in range(1, T + 1):
    start, end = map(int, input().split())
    print(f'#{i} {route(start, end)}')

# 특이한 리모콘 ----------------------------------------------------------------------------
T = int(input())


def button(start, target):
    q = deque([(start, 0)])
    visited = [False] * 100001

    while q:
        now, cnt = q.popleft()
        move = [now // 2, now * 2, now + 1, now - 1]

        if now == target:
            return cnt

        for x in move:
            if 0 <= x < 100001 and visited[x] != True:
                visited[x] = True
                q.append((x, cnt + 1))


for i in range(1, T + 1):
    start, end = map(int, input().split())
    print(f'#{i} {button(start, end)}')