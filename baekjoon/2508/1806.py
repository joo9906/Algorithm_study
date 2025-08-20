import sys
from collections import deque
input = sys.stdin.readline

#sys.stdin = open("input2508.txt", "r")

N = int(input().strip())
q = deque()

for _ in range(N):
    input_val = input().strip().split()
    
    word = input_val[0]
    
    if word == "push_front":
        q.appendleft(int(input_val[-1]))
    elif word == "push_back":
        q.append(int(input_val[-1]))
    elif word == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif word == "back":
        try:
            print(q[-1])
        except:
            print(-1)
    elif word == "pop_front":
        try:
            print(q.popleft())
        except:
            print(-1)
    elif word == "pop_back":
        try:
            print(q.pop())
        except:
            print(-1)
    elif word == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif word == "size":
        print(len(q))

    