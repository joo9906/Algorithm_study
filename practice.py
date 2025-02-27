from collections import deque
import sys

# 표준 입력을 input.in 파일로 설정
sys.stdin = open("input.in", "r")

def func():
    n, m = map(int, input().split())
    target = deque(map(int, input().split()))
    arr = deque([i for i in range(1, n+1)])
    cnt = 0

    while target:
        a = arr.popleft()
        b = target.popleft()
        middle = int(len(arr)/2)

        if b in list(arr)[:middle]:
            while a != b:
                arr.append(a)
                a = arr.popleft()
                cnt += 1
        else:
            while a != b:
                arr.appendleft(a)
                a = arr.pop()
                cnt += 1

    return print(cnt)

func()
