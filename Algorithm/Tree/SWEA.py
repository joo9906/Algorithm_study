# Tree day 2 - 이진탐색
import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

class binary:
    def __init__(self, n):
        self.tree = [0] * (n + 2)
        self.arr = [i for i in range(n+1)]
        self.depth = 1
        self.n = n


    def build(self, left, right, i = 1):
        if i > self.n:
            return

        mid = (left+right) // 2
        self.build(left, mid-1, i * 2)
        self.tree[i] = self.arr[self.depth]
        self.depth += 1
        self.build(mid+1, right, i * 2 + 1)


    def search(self):
        target = int(self.n / 2) # Tq 2번 노드에 저장된 값으로 나누고 있어서 1시간동안 답이 안나옴
        return print(self.tree[1], self.tree[target])

for k in range(1, T+1):
    N = int(input())
    tree = binary(N)
    tree.build(1, N)
    print(f'#{k}', end = ' ')
    tree.search()

