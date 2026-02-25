def solution(n, costs):
    answer = 0
    island = sorted(costs, key=lambda x: x[2])
    parents = [i for i in range(n)]
    cnt = 0

    def find(x):
        if x == parents[x]:
            return x

        parents[x] = find(parents[x])  # 경로압축, 같은 그룹이면 쳐낼거니까
        return parents[x]

    def union(x, y):
        rootx = find(x)
        rooty = find(y)

        if rooty == rootx:  # 같은 그룹이면 암것도 안함. 사이클이니까 터트려
            return

        if rootx < rooty:
            parents[rooty] = rootx
        else:
            parents[rootx] = rooty

    for start, end, cost in island:
        # 연결이 되지 않은 상태라면 연결하고 비용 추가
        if find(start) != find(end):
            union(start, end)
            answer += cost
            cnt += 1

        else:  # 이미 연결되어 있다면 넘어감
            continue

        # 다 연결시켰으면 중지
        if cnt == n - 1:
            break

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))