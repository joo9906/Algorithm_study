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
        self.tree[i] = self.build(left, mid, i * 2) + self.build(mid + 1, right, i * 2 + 1)
        return self.tree[i]

    def search(self, start, end, left, right, i = 1):
        if end < left or right < start: # 이 부분 주의하기
            return 0

        if left <= start and end <= right: # 여기도 주의하기
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

# 구간곱 - 더럽게 고칠거 많네

MOD = 1000000007 # 얘를 해줘야 백준 기준으로 터질 확률이 낮아진다

class gob_tree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [1] * (self.n * 4) # 항등원으로 초기 값을 설정
        self.build(0, self.n - 1)

    def build(self, left, right, i = 1):
        if left == right:
            self.tree[i] = self.arr[left]
            return self.tree[i]

        mid = (left + right) // 2
        self.tree[i] = (self.build(left, mid, i * 2) * self.build(mid + 1, right, i * 2 +1)) % MOD
        return self.tree[i]

    def search(self, start, end, left, right, i = 1):
        if right < start or end < left:
            return 1

        if left <= start and right >= end:
            if self.tree[i] == 0: # 범위 안에 있는데 본인이 0인 값이 있으면 바로 0을 뱉어버림
                return 0
            return self.tree[i] # 그 외에는 모두 자기자신 뱉음
        
        mid = (start + end) // 2
        left_search = self.search(start, mid, left, right, i * 2)
        
        if left_search == 0: # 0이 포함된 구간이라면 0을 뱉음
            return 0
        
        right_search = self.search(mid + 1, end, left, right, i * 2 +1)

        return (left_search * right_search) % MOD

    def update(self, start, end, target, change, i = 1):
        if end < target or target < start:
            return # 구간을 벗어나면 아무것도 안함

        if start == end: # 리프노드에 도달하면 값을 바꿔줌
            if self.tree[i] == change:
                return
            self.tree[i] = change % MOD
            return
        else:
            mid = (start + end) //2
            self.update(start, mid, target, change, i * 2)
            self.update(mid+1, end, target, change, i * 2 + 1)

            # 얘를 밑으로 내려서 리프 노드부터 바꾸면서 올라오는걸로 변경
            self.tree[i] = (self.tree[i * 2] * self.tree[i * 2 + 1]) % MOD

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


