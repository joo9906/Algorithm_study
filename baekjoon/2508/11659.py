import sys
input = sys.stdin.readline
sys.stdin = open("input2508.txt", "r")

class Segtree:
    def __init__(self, start, end):
        self.start = start
        self.end = end

N, M = map(int, input().strip().split())
arr = [0] + list(map(int, input().strip().split()))
for _ in range(M):
    i, j = map(int, input().strip().split())
    print(sum(arr[i:j+1]))