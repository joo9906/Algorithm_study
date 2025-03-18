import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


arr = []
while True:
    start, end = map(int, input().split())
    if start == 0 and end == 0:
        break

    arr.append((start,end))