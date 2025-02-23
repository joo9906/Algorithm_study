from collections import deque

dice = deque([0] * 7) # 주사위 6면(0번째는 세지 않으면 됨)
comp = deque(list(map(int, input().split())))
print(comp)