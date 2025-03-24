# Prim 알고리즘
import heapq

def prim(start_node):
    pq = [(0, start_node)] # 가중치와 노드 - 시작점의 가중치는 0
    MST = [False] * V # visited랑 동일
    min_weight = 0

    while pq:
        w, node = heapq.heappop(pq)

        if MST[node]:
            continue

        MST[node] = True
        min_weight += w

        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue

            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)] # 인접 행렬, 리스트로 구하기는 도전과제

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight # 양방향도 해둠
    graph[end][start] = weight

result = prim(4)
print(result)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

''' 
Kurskal 알고리즘
 - 모든 간선들을 보며 가중치가 작은 간선부터 고르자 (오름차순으로 정렬하기)
 - 이 때, 사이클이 발생하면 넘어감
 - 간선이 적을수록 효과적임(정렬이 필요하지 않기 때문)
'''

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x]) # 경로압축, 같은 그룹이면 쳐낼거니까
    return parents[x]

def union(x, y):
    rootx = find_set(x)
    rooty = find_set(y)

    if rooty == rootx: # 같은 그룹이면 암것도 안함. 사이클이니까 ;터트려려
       return

    if rootx < rooty:
        parents[rooty] = rootx
    else:
        parents[rootx] = rooty


V, E = map(int, input().split())
edge = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    edge.append((start, end, weight))

edge.sort(key = lambda x: x[2])
parents = [i for i in range(V)] # 대표자 찾기

cnt = 0 # n-1까지 반복할거니까 얼마나 했는지 알기 위해
result = 0 #MST 가중치의 합

for u, v, w in edge:
    if find_set(u) != find_set(v):
        union(u, v)
        cnt +=1
        result += w

        if cnt == V-1:
            break

print(result)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 다익스트라 알고리즘

import heapq

def dijkstar(start_node):
    pq = [(0, start_node)]
    distance = [float('inf')] * V # 해당 노드까지 가는 최단거리 저장 리스트
    distance[start_node] = 0 # 시작 노드의 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        if distance[node] < dist:
            continue

        for info in graph[node]: # info = 노드의 번호, 가중치
            next_wegiht = info[0] # 다음 노드로 가기 위한 가중치
            next_node = info[1] # 다음 노드

            ndist = dist + next_wegiht

            if ndist >= distance[next_node]:
                break

            distance[next_node] = ndist

            heapq.heappush(pq, (ndist, next_node))

    return distance

V, E = map(int, input().split())
start_node = 0 # 문제마다 시작 노드가 어디일지는 다름
graph = [[] for _ in range(V)] # 노드의 수 만큼 제작(인접리스트)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 다음 노드, 가중치

