import sys
from collections import deque
sys.input = open("input.txt","r")

N, K = map(int, input().split())
MAX = 100000
visited = [False] * (MAX + 1)
q = deque([(N, 0)])
visited[N] = True
answer = 100000000

while q:
    now, second = q.popleft()
    if now == K and answer > second:
        answer = min(answer, second)
        break

    # 순간이동 (시간 0)
    if 0 <= now * 2 <= MAX and not visited[now * 2]:
        visited[now * 2] = True
        q.append((now * 2, second))

    # +1 이동
    if 0 <= now + 1 <= MAX and not visited[now + 1]:
        visited[now + 1] = True
        q.append((now + 1, second + 1))

    # -1 이동
    if 0 <= now - 1 <= MAX and not visited[now - 1]:
        visited[now - 1] = True
        q.append((now - 1, second + 1))

print(answer)