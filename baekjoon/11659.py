import sys
input = sys.stdin.readline
#sys.stdin = open("input.txt", 'r')

n, m = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

start = 0
end = 1
total = sum(nums[start:end])
for _ in range(m):
    s, e = map(int, input().strip().split())
    if s > start:
        total -= nums[start]
        start += 1
    elif s < start:
        total += nums[start]
        start -= 1

    if e > end:
        
        total += nums[end]
        end += 1
    elif e < end:
        total -= nums[end]
        end -= 1
    print(start, end, total)
    print(total)