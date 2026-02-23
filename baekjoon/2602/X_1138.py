import sys
#input = sys.stdin.readline
sys.stdin = open("../input.txt", "r")

n = int(input())
arr = list(map(int, input().strip().split()))
ans = [0] * n

for _ in range(5):
    target = max(arr)
    print(arr)
    for i in range(n):
        if arr[i] != -1:
            if arr[i] == target:
                ans[i] = n
                n -= 1
                arr[i] = -1
            continue

        else:
            continue

print(ans)