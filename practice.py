from collections import deque

class gob_tree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (self.n * 4)
        self.build(0, self.n - 1)

    def build(self, left, right, i = 1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]

        mid = (left + right) // 2
        self.tree[i] = self.build(left, mid, i * 2) * self.build(mid + 1, right, i * 2 +1)
        return self.tree[i]

    def search(self, start, end, left, right, i = 1):
        if right < start or end < left:
            return 1

        if left <= start and right >= end:
            return self.tree[i]

        mid = (start + end) // 2
        return self.search(start, mid, left, right, i * 2) * self.search(mid + 1, end, left, right, i * 2 +1)

    def update(self, start, end, target, change, i = 1):
        if end < target or target < start:
            return # 구간을 벗어나면 아무것도 안함

        if start != end: # 리프노드가 아니라면 좌우로 내려감
            mid = (start + end) //2
            self.update(start, mid, target, change, i * 2)
            self.update(mid+1, end, target, change, i * 2 + 1)

        # 얘를 밑으로 내려서 리프 노드부터 바꾸면서 올라오는걸로 변경
        self.tree[i] = self.tree[i] * change # 노드 * (원래 값 / 바꾸는 값)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tc = deque([list(map(int, input().split())) for _ in range(m+k)])

tree = gob_tree(arr)
while tc:
    testcase = tc.popleft()

    if testcase[0] == 1:
        tree.update(0, n-1, testcase[1], testcase[2])
    elif testcase[1] == 2:
        tree.search(0, n-1, testcase[1]-1, testcase[2]-1)