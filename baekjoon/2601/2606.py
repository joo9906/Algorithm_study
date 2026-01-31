from collections import deque
import sys
#input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

c = int(input().strip())
computer = {i:set() for i in range(1, c+1)}

n = int(input().strip())
check = []
for _ in range(n):
    start, end = map(int, input().strip().split())
    computer[start].add(end)
    computer[end].add(start)

q = deque([1])
ans = set()

while q:
    now = q.popleft()
    nxt_node = computer[now]

    for i in nxt_node:
        if i in ans:
            continue
        else:
            ans.add(i)
        q.append(i)

if ans:
    print(len(ans)-1)
else:
    print(0)


