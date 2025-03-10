import sys
from collections import deque
import heapq
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