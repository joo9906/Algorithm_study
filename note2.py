import sys
input = sys.stdin.readline

a = list(map(int, input().strip().split()))
res = 0
for i in a:
    res += i**2
print(res%10)