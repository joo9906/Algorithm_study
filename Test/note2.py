import heapq
import sys
#from collections import deque
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def find(x):
    global parents

    if x == parents[x]:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    global parents

    rx = find(x)
    ry = find(y)

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(E)]
    data.sort(key=lambda x: x[2])
    parents = [i for i in range(V+1)] # 노드가 1번부터 시작하니까 0번째는 버릴거임

    cnt = 0
    min_weight = 0

    for k in data:
        start, target, weight = k
        if find(start) != find(target): # 둘이 연결이 되어있지 않은 상태일 때 실행
            union(start, target)
            cnt += 1
            min_weight += weight

        if cnt == V-1:
            break

    print(f'#{tc} {min_weight}')