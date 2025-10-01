import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

N = int(input())
balloons = list(map(int, input().strip().split()))
q = deque()
ans = []

for i in range(N):
    q.append((i+1, balloons[i]))

stack = 0
bal_num, move = q.popleft()
ans.append(bal_num)
stack = move

while q:
    if stack > 0:
        for _ in range(stack):
            stack -= 1
            if stack == 0:
                nb, nm = q.popleft()
                ans.append(nb)
                stack = nm
                break
            q.append(q.popleft())

    elif stack < 0:
        for _ in range(-stack):
            stack += 1
            if stack == 0:
                nb, nm = q.popleft()
                ans.append(nb)
                stack = nm
                break
            q.appendleft(q.pop())

print(*ans)
