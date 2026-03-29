import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

N = int(input())
balloons = list(map(int, input().strip().split()))
balloon_list = deque()
for i in range(N):
    balloon_list.append((i+1, balloons[i]))

result = []
while balloon_list:
    balloon_num, nxt = balloon_list.popleft()

    result.append(balloon_num)

    try:
        if nxt < 0:
            for _ in range(-nxt):
                balloon_list.appendleft(balloon_list.pop())
        else:
            for _ in range(nxt-1):
                balloon_list.append(balloon_list.popleft())
    except:
        break

print(*result)