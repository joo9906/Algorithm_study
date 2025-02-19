from collections import deque

n = int(input())
stack = deque()
garbage = []
for i in range(1, n+1):
    stack.append(i)
while len(stack) > 1:
    a = stack.popleft()
    garbage.append(a)
    b = stack.popleft()
    stack.append(b)

print(*stack)