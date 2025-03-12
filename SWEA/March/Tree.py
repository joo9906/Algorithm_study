# 사칙연산
class Tree:
    def __init__(self):
        self.tree = {i:[] for i in range(1, 1001)}

    def build(self,arr):
        for li in arr: # 트리를 생성하는 부분, 길이가 4 일 경우 몇 번 노드와 연결되어 있는지 저장
            if len(li) == 4:
                self.tree[int(li[0])] = (li[1], int(li[2]), int(li[3]))

            elif len(li) == 2:
                self.tree[int(li[0])] = int(li[1])

    def calcul(self, start):
        target = self.tree[start]

        if type(target) == int:
            return target

        op, left_val, right_val = target

        if target[0] == '+':
            left = self.calcul(left_val)
            right = self.calcul(right_val)
            return left + right

        elif target[0] == '-':
            left = self.calcul(left_val)
            right = self.calcul(right_val)
            return left - right

        elif target[0] == '*':
            left = self.calcul(left_val)
            right = self.calcul(right_val)
            return left * right

        elif target[0] == '/':
            left = self.calcul(left_val)
            right = self.calcul(right_val)
            return left // right

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(str, input().split())) for _ in range(n)]

    sol = Tree()
    sol.build(arr)
    print(f'#{tc} {sol.calcul(1)}')

# 중위순회
class inorder():
    def __init__(self, n):
        self.n = n
        self.arr = [0] + [tuple(map(str, input().split())) for _ in range(n)]
        self.tree = [0] * (n + 2)
        self.result = ''
        self.build(0, n - 1)

    def build(self, start, end, i=1):
        if i > self.n:
            return

        mid = (start + end) // 2

        self.build(start, mid - 1, i * 2)
        self.result += self.arr[i][1]
        self.build(mid + 1, end, i * 2 + 1)


for i in range(1, 11):
    tree = inorder(int(input()))
    print(f'#{i} {tree.result}')

# subtree
from collections import deque

class subtree:
    def __init__(self):
        self.tree = {}

    def build(self, N, arr):
        self.tree = {i: [] for i in range(1, N + 2)}
        for k in range(N):
            root = arr[k * 2]
            child = arr[k * 2 + 1]
            self.tree[root].append(child)

    def search(self, target):
        cnt = 0
        stack = deque([target])
        while stack:
            t = stack.popleft()
            cnt += 1
            stack.extend(self.tree[t])
        return cnt


T = int(input())

for i in range(1, T + 1):
    n, target = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = subtree()
    tree.build(n, arr)
    print(f'#{i} {tree.search(target)}')

# 이진 탐색
T = int(input())


class binary:
    def __init__(self, n):
        self.tree = [0] * (n + 2)
        self.depth = 1
        self.n = n

    def build(self, i=1):
        if i > self.n:
            return

        self.build(i * 2)
        self.tree[i] = self.depth
        self.depth += 1
        self.build(i * 2 + 1)

    def search(self):
        target = int(self.n / 2)  # Tq 2번 노드에 저장된 값으로 나누고 있어서 1시간동안 답이 안나옴
        return print(self.tree[1], self.tree[target])


for k in range(1, T + 1):
    N = int(input())
    tree = binary(N)
    tree.build()
    print(f'#{k}', end=' ')
    tree.search()

# 이진 힙
import heapq

T = int(input())


def min_heap(n, arr):
    tree = []

    for i in arr:
        heapq.heappush(tree, i)

    minsum = 0
    idx = n - 1

    while idx > 0:
        idx = (idx - 1) // 2
        minsum += tree[idx]

    return minsum


for k in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{k} {min_heap(n, arr)}')

# 노드의 합
T = int(input())


def tree_sum():
    n, m, l = map(int, input().split())

    tree = [0] * (n + 5)
    save = [list(map(int, input().split())) for _ in range(m)]

    for node, num in save:
        tree[node] = num
    for idx in range(n, 0, -1):
        if tree[idx] == 0:
            tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]

    return tree[l]


for k in range(1, T + 1):
    print(f'#{k} {tree_sum()}')