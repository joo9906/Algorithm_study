import sys
# sys.stdin = open("input2508.txt", "r")
input = sys.stdin.readline
N, M = map(int, input().strip().split())
ans = {}
sol = [0]
for i in range(1, N+1):
    name = input().strip()
    ans[name] = i
    sol.append(name)

for _ in range(M):
    val = input().strip()

    if val.isdigit():
        print(sol[int(val)])
    else:
        print(ans[val])