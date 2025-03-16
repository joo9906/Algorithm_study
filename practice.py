import sys, copy
sys.stdin = open('input.txt', 'r')
#input = sys.stdin.readline

def find_max_distance(T):
    for tc in range(1, T + 1):
        K = int(input())
        S = input()

        A_positions = [i for i, c in enumerate(S) if c == 'A']

        if len(A_positions) < K:
            print(f"#{tc} 0")
            continue

        max_distance = 0

        for i in range(len(A_positions) - K + 1):
            start = A_positions[i]
            end = A_positions[i + K - 1]

            distance = end - start
            max_distance = max(max_distance, distance)

        print(f"#{tc} {max_distance}")

T = int(input())
find_max_distance(T)