
# 백준 1931 회의실 배정 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 그리디 써서 푸는건데 어떤게 나올 지 가늠이 안됨.
def solve(n, time):
    time.sort(key=lambda x : (x[1], x[0]))
    result = [time[0]]

    i = 1
    k = 0
    while i < n:
        start, end = time[i]

        # 시작 시간이 이전 회의시간의 끝나는 시간과 같거나 큰 경우 회의 진행 가능
        if start >= result[k][1]:
            result.append((start, end))
            k += 1

        i+=1

    return len(result)


n = int(input().strip())
time = [tuple(map(int, input().strip().split())) for _ in range(n)]
cnt = 0
print(solve(n, time))

# MST ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 최소 스패닝 트리 - SWEA

# prim 버전
class Prim:
    def __init__(self, V, E, data, adj):
        self.V = V
        self.E = E
        self.data = data
        self.adj = adj

    def solve(self, start_node):
        MST = [False] * (self.V+1) # 방문을 했다고 넣을 것
        q = [(0, start_node)] # 맨 처음 뽑을 대상의 가중치는 0, 시작 노드
        min_weight = 0

        while q:
            weight, node = heapq.heappop(q)

            if MST[node]: # 뽑아다가 쓴 적 있는 간선이라면 지나감
                continue

            MST[node] = True
            min_weight += weight # 간선의 최소 가중치에 더함 - 여기에서 더하는 이유는 최소 가중치 간선을 뽑아온거기 때문

            for i in range(node, self.V + 1):
                if self.adj[node][i] == float('inf'):
                    continue

                if MST[i]:
                    continue

                # 인접 행렬에서 의미가 있는 자료인 경우에만 아래를 실행
                new_w = self.adj[node][i]
                heapq.heappush(q, (new_w, i))

        return min_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(E)]
    adj = [[] for _ in range(V + 1)]
    for node, target, w in data:
        adj[node][target] = w
        adj[target][node] = w

    ans = Prim(V, E, data, adj)
    print(f'#{tc} {ans.solve(1)}')

# 크루스칼 버전
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
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(E)]
    data.sort(key=lambda x: x[2])
    parents = [i for i in range(V + 1)]  # 노드가 1번부터 시작하니까 0번째는 버릴거임

    cnt = 0
    min_weight = 0

    for k in data:
        start, target, weight = k
        if find(start) != find(target):  # 둘이 연결이 되어있지 않은 상태일 때 실행
            union(start, target)
            cnt += 1
            min_weight += weight

        if cnt == V - 1:
            break

    print(f'#{tc} {min_weight}')

# MST - 백준 네트워크 연결(1922) ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 이거 인접 리스트로 안받으면 터질 수 있음
# 프림이 더 유리한 경우는 노드의 개수가 충분히 많고 간선이 노드의 2배를 넘어갈 때

# 프림 버전
class Prim:
    def __init__(self, n, m):
        self.n = n  # 노드의 개수
        self.m = m  # 간선의 개수

    def solve(self, graph):
        # 최소 힙을 이용해서 Prim 알고리즘
        MST = [False] * (self.n + 1)  # 방문 여부 배열
        min_weight = 0  # 최소 가중치 합

        # (가중치, 노드 번호)
        q = [(0, 1)]  # 시작 노드는 1로 설정
        while q:
            weight, node = heapq.heappop(q)

            if MST[node]:  # 이미 MST에 포함된 노드라면 넘어감
                continue

            min_weight += weight  # 해당 노드를 MST에 포함시킨다.
            MST[node] = True

            # 인접한 노드들 탐색
            for nw, nn in graph[node]:
                if not MST[nn]:  # 이미 포함된 노드는 제외
                    heapq.heappush(q, (nw, nn))

        return min_weight


# 입력 처리
n = int(input().strip())
m = int(input().strip())
data = [tuple(map(int, input().strip().split())) for _ in range(m)]

# 그래프 초기화 (인접 리스트 형태)
graph = [[] for _ in range(n + 1)]
for start, end, weight in data:
    graph[start].append((weight, end))
    graph[end].append((weight, start))  # 양방향 그래프

# Prim 알고리즘 실행
ans = Prim(n, m)
print(ans.solve(graph))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 크루스칼 버전
class Train:
    def __init__(self, n, m, data):
        self.n = n
        self.m = m
        self.parents = [0] + [i for i in range(1, n+1)]
        self.computer = sorted(data, key=lambda x: (x[2], x[1]))

    def find(self, x):
        if x == self.parents[x]:
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx < ry:
            self.parents[ry] = rx
        else:
            self.parents[rx] = ry

    def kruskal(self):
        cnt = 0
        result = 0

        for start, end, weight in self.computer:
            if self.find(start) != self.find(end):
                self.union(start, end)
                cnt += 1
                result += weight

                if cnt == self.n-1:
                    return result

n= int(input().strip())
m = int(input().strip())
data = [tuple(map(int, input().strip().split())) for _ in range(m)]
solve = Train(n, m, data)
print(solve.kruskal())

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

'''
다익스트라
최단경로를 구하는 문제에서 사용되는 알고리즘
하나의 정점에서 끝 정점까지의 최단 경로
prim 알고리즘과 비슷하지만 다익스트라는 가중치를 누적 시키며 최단 거리를 찾음.
prim은 단순히 각 간선들 중 최소 가중치인 간선을 선택하는 것

따라서 prim이나 kruskal은 모든 노드를 연결시킨다는 MST(최소 신장 트리)이지만 
다익스트라는 최단 거리만을 찾는 것이기 때문에 모든 노드를 연결하지 않음. Dijkstar != MST

다익스트라는 음의 가중치를 사용하지 못함.
이유는 하나의 노드에서 가장 가중치가 낮은 간선을 선택하는데
1-3으로 가는 간선의 가중치가 10, 1-2 가중치 15 1-3 가중치 -10 일 경우 1-2-3의 누적
가중치가 더 작은데 1-3 간선으로 이미 확정시켜서 1-2-3을 써먹지를 못함.
즉 음수와 양수가 섞이면 이거 판단을 못함
이를 해결하기 위해서는 벨만-포드 알고리즘을 써야 한다.

다만 다익스트라와 벨만 포드는 처음 노드에서 끝 노드까지의 최단거리를 구하는 방법이고
모든 정점의 최단 거리를 구하는건 플로이드-마샬 알고리즘임



신장 트리
1. 노드의 개수가 n이고 간선의 개수가 n-1인 트리
2. 모든 노드가 서로 양방향으로 연결 되어 있음
3. 간선의 개수가 n-1이므로 사이클이 없음이 보장된 트리
4. 하나의 그래프에서 여러 개의 트리가 나올 수 있음
+ 간선의 가중치가 가장 작은 것들로 이루어진 게 최소신장트리(MST)

Prim 알고리즘과 Kruskal 
간선의 개수가 많아질수록 Prim 알고리즘이 효율적임
-> kruskal은 정렬을 해야 사용 가능하기 때문
kruskal은 union find의 방법을 사용해서 노드끼리 연결되어 있는지 확인하며 최소가중치만 고름
정렬이 되어 있기 때문에 노드를 순서대로 확인하지 않고 무조건 최소 간선만 확인해서 연결

prim은 인접행렬/리스트에 정보를 저장하고 우선순위큐를 활용해서 품(visit도 사용)
노드 하나를 보고 거기서 가장 가중치가 낮은 애만 선택하는 과정 반복

'''