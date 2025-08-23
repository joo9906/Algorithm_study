import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

def solve(N, point):
    answer = 0

    if len(point) == 3:
        answer = point[-1] - point[0]
        return answer

    pass_point = min(point)
    pass_point_location = point.index(pass_point)

    now = 0
    for i in range(1, N):
        if i == pass_point_location:
            continue
        else:
            distance = abs(point[i] - point[now])
            answer += distance
            now += 1

    return answer

for tc in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    print(f'#{tc} {solve(N, point)}')