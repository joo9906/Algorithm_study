import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solve(N, K):
    money = []
    buy = 0
    min_cost = 0

    for _ in range(N):
        Ai, Bi = map(int, input().strip().split())
        money.append((Ai, Bi))

    # 할인 효과가 큰 순서로 정렬 (Bi - Ai가 큰 것부터)
    money.sort(key=lambda x: (x[1] - x[0]), reverse=False)
    for Ai, Bi in money:
        if buy >= K:
            break

        if Ai >= Bi:
            buy += 1
            continue

        min_cost = max(min_cost, Bi - Ai)
        buy += 1


    return min_cost

N, K = map(int, input().strip().split())
print(solve(N, K))
