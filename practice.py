import sys, heapq, copy
from collections import deque
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

class Answer:
    def __init__(self, n ,arr, target):
        self.n = n
        self.arr = arr
        self.tree = {i:[] for i in range(self.n)}
        self.build()
        self.remove(target)
        self.cnt = 0
        self.recur(0)

    def build(self):
        for k in range(self.n):
            if arr[k] == -1:
                continue
            self.tree[self.arr[k]].append(k)

    def remove(self, target):
        if target in self.tree:
            del self.tree[target]

        for p in self.tree:
            if target in self.tree[p]:
                self.tree[p].remove(target)

    def recur(self, node):
        if 0 not in self.tree.keys():
            return

        if not self.tree[node]:
            self.cnt += 1
            return

        for ch in self.tree[node]:
            self.recur(ch)

    def result(self):
        return self.cnt

n = int(input().strip())
arr = list(map(int, input().strip().split()))
target = int(input().strip())

solve = Answer(n, arr, target)
print(solve.cnt)