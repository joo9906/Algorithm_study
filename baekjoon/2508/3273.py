import sys
import itertools
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
arr.sort()
target = int(input().strip())

cnt = 0
end_point = 0
for i in range(n):
    if arr[i] < target:
        end_point = max(end_point, i)

compare = arr[:end_point+1]
mid = end_point//2

for i in range(end_point-1):
    for j in range(end_point):
        if compare[i] + compare[j] == target:
            cnt += 1

print(cnt)