import sys
# sys.stdin = open('input2508.txt','r')
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
arr.sort()
target = int(input().strip())

ans = 0
left, right = 0, n - 1

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        ans += 1
        left += 1
        right -= 1
    elif s < target:
        left += 1
    else:
        right -= 1

print(ans)
