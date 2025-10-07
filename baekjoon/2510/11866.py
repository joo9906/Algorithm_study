
import sys
sys.stdin = open("input.txt", 'r')

from collections import deque
N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
answer = []

cnt = 1
while q:
    now = q.popleft()

    if cnt % K == 0:
        answer.append(now)
    else:
        q.append(now)
    cnt += 1

print(f'<{", ".join(map(str, answer))}>')