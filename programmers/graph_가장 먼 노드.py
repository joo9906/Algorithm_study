def solution(n, edge):
    answer = 0
    connect = {i: [] for i in range(1, n + 1)}
    visited = [False] * (n + 1)
    far_node = []
    far = 0
    for start, end in edge:
        connect[start].append(end)

    def search(node, depth=0):
        nonlocal connect, far_node, far

        # 더이상 들어갈 곳이 없다면 비교 시작
        if not connect[node]:
            # 현재 노드가 가장 먼 노드보다 가깝다면 넘어감
            if far > depth:
                return
            # 현재 노드가 가장 먼 노드와 거리가 같다면 기록
            elif far == depth:
                far_node.append(node)
            # 현재 노드가 가장 먼 노드보다 멀다면 담겨진 것들 초기화 하고 거리를 현재 깊이로 업데이트
            elif far < depth:
                far_node = [node]
                far = depth
            return

        for i in connect[node]:
            if not visited[i]:
                visited[i] = True
                search(i, depth + 1)
                visited[i] = False

    for start in connect[1]:
        visited[start] = True
        search(start)
        visited[start] = False
    print(far_node)
    answer = len(far_node)

    return answer
n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))