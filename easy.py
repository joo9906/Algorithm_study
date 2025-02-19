<<<<<<< HEAD
=======
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
>>>>>>> 2e63bb9d5370cfe0a17588f84bc13a7f70d4d89d
