from collections import deque

def solve(nodes, start, target):
    answer = 1001
    q = deque()
    for val in nodes[start]:
        check = set()
        check.add(val)
        q.append((check, val, 0))

    while q:
        checks, now, cnt = q.popleft()

        if target in checks:
            answer = min(answer, cnt)
            continue
        
        if nodes[now]:
            for next in nodes[now]:
                if next not in checks:
                    checks.add(next)
                    q.append((checks, next, cnt + 1))

    if answer < 1001:
        return answer
    else:
        return 0
    
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodes = {i:[] for i in range(1, V+1)}
    for _ in range(E):
        start, end = map(int, input().split())
        nodes[start].append(end)
    S, G = map(int, input().split())

    print(f'#{tc} {solve(nodes, S, G)}')