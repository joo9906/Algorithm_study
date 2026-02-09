def solution(n, m, x, y, ra, ca, k):
    # 사전순 방향. 처음부터 사전순으로 간다고 생각하면 가장 먼저 도달하는게 사전순으로도 빠른 것
    dirs = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
    result = []

    # 맨허튼 거리를 사용해 남은 거리를 파악.
    dist = abs(x - ra) + abs(y - ca)
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"

    # 원래 while문으로 풀려고 했으나 단순히 k번만 반복하면 되고, 사전순으로 방향까지 미리 설정해두면 시간초과가 나지 않는다는 점을 꺠달음
    # 이렇게 하면 visited도 사용하지 않고 bfs로 풀 필요도 없음. 개빡구현 문제라고 생각해야 하는 듯. DFS, BFS로 접근하니 다터짐
    r, c = x, y
    for _ in range(k):
        for d, dr, dc in dirs:
            nr, nc = r + dr, c + dc
            # 범위 벗어나면 쳐냄
            if not (1 <= nr <= n and 1 <= nc <= m):
                continue

            # 남은 거리로 도착 가능하면 그 방향 도전
            remain = k - len(result) - 1 # 남은 거리(주어진 k - 현재까지 지나온 거리 - 1) => 여기서 -1은 다음에 한 칸 더 가야하니까
            new_dist = abs(nr - ra) + abs(nc - ca) # 비교를 위한 맨허튼 거리.
            if new_dist <= remain and (remain - new_dist) % 2 == 0:
                result.append(d)
                r, c = nr, nc
                break

    return "".join(result)
