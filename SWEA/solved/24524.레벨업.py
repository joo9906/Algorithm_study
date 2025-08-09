import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def solve(N, point):
    print(point)






for tc in range(1, T+1):
    N = int(input())
    point = list(map(int, input().split()))
    print(f'#{tc} {solve(N, point)}')