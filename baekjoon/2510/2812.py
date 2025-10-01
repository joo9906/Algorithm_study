import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
num = list(map(str, input().strip()))
result = []
result.append(int(num[0]))

while K > 0:
