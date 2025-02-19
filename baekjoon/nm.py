#1. 
# --------------------------------------------------------------------
# 2.
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
