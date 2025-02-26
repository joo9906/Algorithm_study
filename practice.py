from collections import deque
import sys

# 표준 입력을 input.in 파일로 설정
sys.stdin = open("input.in", "r")

def tttt():
    N = int(input())
    top = list(map(int, input().split()))
    result = [0] * N
    ind = []

    for i in range(N):
        target = top.pop()
        a = len(top) - 1
        while True:
            if a == 0:
                result.appendleft(0)
                break

            num_index = a
            now_num = top[num_index]

            if now_num >= target:
                result.appendleft(num_index)
                break

            a -= 1


    return print(*result)

tttt()