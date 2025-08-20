import sys
input = sys.stdin.readline
# sys.stdin = open("input2508.txt", "r")

n = int(input().strip())
def solve(arr):
    stack = []
    for i in arr:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                return

    if stack:
        print("NO")
    else:
        print("YES")

for _ in range(n):
    arr = list(map(str, input().strip()))
    solve(arr)

