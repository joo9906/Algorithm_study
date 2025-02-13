from collections import deque

def graph(arr):
    graph = {i: [] for i in range(100)}

    for j in range(0, len(arr), 2):
        start, end = arr[j], arr[j+1]
        graph[start].append(end)

    print(graph)

    a = deque([0])
    visit = [False] * 100
    visit[0] = [True]

    print(visit)
    print(a)
    while a:
        now = a.popleft()

        if now == 99:
            return 1
        
        for j in graph[now]:
            if not visit[j]:
                visit[j] = True
                a.append(j)

    print(graph)

    return 0

arr = list(map(int,input().split()))
print(graph(arr))