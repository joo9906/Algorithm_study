import sys
from collections import defaultdict
#input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

tree = []
while 1:
    try:
        i = int(input().strip())
        tree.append(i)
    except:
        break

def solve(arr):
    if len(arr) == 0:
        return

    Ltree, Rtree = [], []
    mid = arr[0]

    for i in range(1, len(arr)):






