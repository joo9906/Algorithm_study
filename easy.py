n = int(input())
arr = set(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))

result = []

for num in brr:
    if num in arr:
        result.append(1)
    else:
        result.append(0)



print(*result)