import sys
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.head = {}
    
    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['end'] = True
    
    def search(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if 'end' in cur:
            return True
        else:
            return False

tree = Trie()
n, m = map(int, input().split())
cnt = 0

for _ in range(n):
    tree.add(input().strip())

for _ in range(m):
    if tree.search(input().strip()):
        cnt += 1

print(cnt)
