import sys
sys.stdin = open("input.in", 'r')

def dfs(node, visited):
    visited |= (1 << node) # node의 수만큼 shift를 해서 어디를 방문 했는지 표현하는 것.
    print(node, visited)
    for next_node in range(N):
        if graph[node][next_node] == 0:
            continue

        if visited & (1 << next_node): #visited의 자리와 다음 노드의 자리가 1로 같으면 방문한거임
            continue

        dfs(next_node, visited)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    visited = 0 # 초기 방문 상태
    dfs(0, visited)

