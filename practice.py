import sys
sys.stdin = open("input.in", "r")

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

f_n = a1*n + a0
result = c * n

if f_n <= result:
    print(1)
else:
    print(0)