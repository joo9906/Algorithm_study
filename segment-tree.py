# 구간합
class sum_tree:
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
        self.tree[i] = self.build(left, mid, i * 2) + self.build(mid + 1, right, i * 2 +1)
        return self.tree[i]

    def search(self, start, end, left, right, i = 1):
        if left < start or end < right:
            return 0

        if left >= start and right <= end:
            return self.tree[i]

        mid = (start + end) // 2
        return self.search(start, mid, left, right, i * 2) + self.search(mid + 1, end, left, right, i * 2 +1)

    def update(self, left, right, target, diff, i = 1):
        if left > target or right < target: # 구간을 넘어갔으면 안함
            return
        self.tree[i] += diff
        if left != right:
            mid = (left + right) // 2
            self.update(left, mid, target, diff, i * 2)
            self.update(mid+1, right, target, diff, i * 2 +1)

arr = [1, 3, 4, 2, 5, 6, 7]
# stree = sum_tree(arr)
# print(stree.tree)
# print(stree.search(0, 6, 3, 4))
# stree.update(0, 6, 3, 2)
# print(stree.tree)
# print(stree.search(0, 6, 3, 4))

# 최솟값
class min_segment:
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
        self.tree[i] = min(self.build(left, mid, i * 2),self.build(mid + 1, right, i * 2 +1))
        return self.tree[i]

    def search(self, start, end, left, right, i = 1):
        if right < start or left > end:
            return float('inf')

        if start >= left and end <= right:
            return self.tree[i]

        mid = (start + end) // 2
        return min(self.search(start, mid, left, right, i * 2), self.search(mid+1, end, left, right, i * 2 +1))

    def update(self, start, end, target, change, i = 1):
        if start > target or end < target:
            return

        if start == end and start == target:
            print('리프노드 변경')
            self.tree[i] = change
            return

        if start != end:
            mid = (start + end) //2
            self.update(start, mid, target, change, i * 2)
            self.update(mid+1, end, target, change, i * 2 +1)

        self.tree[i] = min(self.tree[i*2], self.tree[i * 2 +1])

# mtree = min_segment(arr)
# print(mtree.tree)
# print(mtree.search(0, 6, 1, 5))
# mtree.update(0, 6, 2, 9)
# print(mtree.tree)

# 최댓값
class max_segment:
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
        self.tree[i] = max(self.build(left, mid, i * 2),self.build(mid + 1, right, i * 2 +1))
        return self.tree[i]

    def search(self, start, end, left, right, i = 1):
        if right < start or left > end:
            return 0

        if start >= left and end <= right:
            return self.tree[i]

        mid = (start + end) // 2
        return max(self.search(start, mid, left, right, i * 2), self.search(mid+1, end, left, right, i * 2 +1))

# mtree = max_segment(arr)
# print(mtree.search(0, 6, 1, 5))
# print(mtree.tree)

# 구간곱
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

gtree = gob_tree(arr)
print(gtree.search(0, 6, 1, 4))
print(gtree.tree)

# Trie
class Trie:
    tree = {}

    def add(self, word):
        cur = self.tree
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur[ch] = True


    def find(self, word):
        cur = self.tree

        for ch in word:
            if ch in word:
                cur = cur[ch]
            else:
                return False

        if cur[ch] == True:
            return True
        else:
            return False

    def remove(self, word):
        cur = self.tree

        for i in word:
            if i in word:
                cur = cur[i]

        cur[i] = False

# t = Trie()
# t.add('hello')
# print(t.tree)
# print(t.find('hello'))
# print(t.find('hel'))
# t.remove('hello')
# print(t.tree)
# print(t.find('hello'))


