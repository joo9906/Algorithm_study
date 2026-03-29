import sys
# input = sys.stdin.readline
sys.stdin = open("input250.txt", "r")

n, target = int(input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()
ans_set = set()

left = 0
right = n-1

while left < right:
    break


