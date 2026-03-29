from collections import deque
import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", 'r')

n = int(input().strip())
q = deque()

for _ in range(n):
    order = input().strip()

    if len(order) == 1:
        if order == '6':
            if q:
                print(0)
            else:
                print(1)
        elif order == '3':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif order == '4':
            if q:
                print(q.pop())
            else:
                print(-1)
        elif order == '5':
            print(len(q))
        elif order == '7':
            if q:
                print(q[0])
            else:
                print(-1)
        elif order == '8':
            if q:
                print(q[-1])
            else:
                print(-1)
    else:
        f, x = map(int, order.strip().split(' '))
        if f == 1:
            q.appendleft(x)
        elif f == 2:
            q.append(x)
