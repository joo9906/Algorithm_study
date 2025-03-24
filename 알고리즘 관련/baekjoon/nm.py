#1번번
def recur():
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n + 1):
        if visited[i] == True:
            continue
        else:
            visited[i] = True
            result.append(i)

            recur()

            result.pop()
            
            visited[i] = False


n, m = map(int, input().split())
result = []
visited = [False] * (n + 1)

recur()
# --------------------------------------------------------------------
# 2번번
n, m = map(int, input().split())
stack = []
arr = [i for i in range(1, n+1)]
visited = [False] * (n)

def nm(cnt):
    if len(stack) == m:
        print(*stack)
        return 
    
    for i in range(cnt, n+1):
        if i not in stack:
            stack.append(i)
            nm(i+1)
            stack.pop()

nm(1)

# ---------------------------------------------------------------------------
# 3번
n, m = map(int, input().split())
stack = []

def recur(n):
    if len(stack) == m:
        print(*stack)
        return

    for i in range(1, n+1):
        stack.append(i)
        recur(n)
        stack.pop()

recur(n)

# ---------------------------------------------------------------------------
# 4번
n, m = map(int, input().split())
stack = []
visited = [False] * (n+1)

def recur(start):
    if len(stack) == m:
        print(*stack)
        return

    for i in range(start, n+1):
        stack.append(i)
        recur(i)
        stack.pop()

recur(1)
#----------------------------------------------------------------------------
# 5번
