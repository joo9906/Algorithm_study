def recur():
    if len(result) == m:
        print(*result)
        return
    
    for i in range(1, n+1):
        if visited[i] == True:
            continue
        else:
            visited[i] = True
            result.append(i)

            recur()

            result.pop()
            print(visited)
            visited[i] = False


n , m = map(int, input().split())
result = []
visited = [False] * (n+1)

recur()
    
